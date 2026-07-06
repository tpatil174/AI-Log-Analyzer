import json
import boto3
import urllib.request

def get_secret(secret_name, region_name='eu-central-1'):
    client = boto3.client('secretsmanager', region_name=region_name)
    response = client.get_secret_value(SecretId=secret_name)
    secret = json.loads(response['SecretString'])
    return secret['OPENAI_API_KEY']

def analyze_log_with_openai(log_content, api_key):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }
    payload = json.dumps({
        'model': 'gpt-3.5-turbo',
        'messages': [
            {
                'role': 'system',
                'content': 'You are an expert IT system administrator. Analyze the server log and provide: 1) A brief summary, 2) Critical errors found, 3) Warnings found, 4) Recommendations to fix the issues. Be concise and clear.'
            },
            {
                'role': 'user',
                'content': 'Analyze this server log:\n\n' + log_content[:4000]
            }
        ],
        'max_tokens': 800
    }).encode('utf-8')

    req = urllib.request.Request(url, data=payload, headers=headers, method='POST')
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))
        return result['choices'][0]['message']['content']

def lambda_handler(event, context):
    s3 = boto3.client('s3', region_name='eu-central-1')
    sns = boto3.client('sns', region_name='eu-central-1')

    sns_topic_arn = 'arn:aws:sns:eu-central-1:363479758460:LogAnalyzer-Alerts'
    secret_name = 'loganalyzer/openai-api-key'

    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        print('Processing file: ' + key + ' from bucket: ' + bucket)

        response = s3.get_object(Bucket=bucket, Key=key)
        log_content = response['Body'].read().decode('utf-8')
        print('Log file size: ' + str(len(log_content)) + ' characters')

        api_key = get_secret(secret_name)
        print('OpenAI API key retrieved successfully')

        analysis = analyze_log_with_openai(log_content, api_key)
        print('Log analysis completed')

        message = 'AI Log Analyzer Report\n'
        message += '======================\n'
        message += 'File: ' + key + '\n'
        message += 'Bucket: ' + bucket + '\n\n'
        message += analysis + '\n\n'
        message += '---\nPowered by LogAnalyzer-AWS | Tushar Patil'

        sns.publish(
            TopicArn=sns_topic_arn,
            Subject='Log Analysis Report: ' + key,
            Message=message
        )

        print('SNS notification sent successfully')
        return {'statusCode': 200, 'body': 'Log ' + key + ' analyzed and report sent successfully.'}

    except Exception as e:
        error_msg = 'LogAnalyzer FAILED: ' + str(e)
        print(error_msg)
        sns.publish(
            TopicArn=sns_topic_arn,
            Subject='LogAnalyzer - Analysis FAILED',
            Message=error_msg
        )
        raise e
