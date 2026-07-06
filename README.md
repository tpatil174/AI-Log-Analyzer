# 🤖 AI Log Analyzer on AWS

![AWS](https://img.shields.io/badge/AWS-Serverless-orange?logo=amazonaws)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Lambda](https://img.shields.io/badge/AWS-Lambda-FF9900?logo=awslambda)
![Amazon S3](https://img.shields.io/badge/Amazon-S3-green?logo=amazons3)
![CloudWatch](https://img.shields.io/badge/CloudWatch-Monitoring-purple?logo=amazoncloudwatch)
![SNS](https://img.shields.io/badge/SNS-Notifications-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-black?logo=openai)
![License](https://img.shields.io/badge/License-MIT-green)

An **AI-powered serverless log analysis system** built entirely on **AWS** that automatically analyzes uploaded log files using **OpenAI**, detects potential issues and security events, generates intelligent summaries, and sends email reports using Amazon SNS.

This project demonstrates modern cloud architecture, serverless computing, infrastructure automation, AI integration, monitoring, and security best practices.

---

# 📌 Table of Contents

- Project Overview
- Why This Project?
- Architecture
- Workflow
- Features
- AI Analysis Pipeline
- AWS Services Used
- Technologies Used
- Project Structure
- Screenshots
- Setup Guide
- Testing
- Live Results
- Security
- Skills Demonstrated
- Future Improvements
- Cost Estimation
- License

---

# 🚀 Project Overview

Modern production systems generate thousands of log files every day.

Manually reading logs to identify:

- Application errors
- Database failures
- Security incidents
- Infrastructure warnings
- Performance bottlenecks

is slow and inefficient.

This project automates that entire workflow.

Whenever a log file is uploaded into Amazon S3:

1. Lambda automatically starts
2. The log is downloaded
3. OpenAI analyzes the content
4. A professional incident report is generated
5. The report is emailed instantly
6. CloudWatch stores execution logs

No servers.

No manual intervention.

Everything is event-driven.

---

# 🎯 Why This Project?

Traditional monitoring systems only send alerts when predefined rules are matched.

This project goes a step further by using AI to understand the context of log files.

Instead of receiving raw log entries, administrators receive:

- Executive summary
- Severity assessment
- Possible root causes
- Security observations
- Recommended next steps

This simulates how modern DevOps, Cloud Engineers, and Site Reliability Engineers (SREs) use AI for intelligent observability.

---

# 🏗 Architecture

![Architecture](images/architecture.png)

```

```text
                  Upload Log File
                        │
                        ▼
                Amazon S3 Bucket
                        │
              Object Created Event
                        │
                        ▼
              AWS Lambda Function
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
Secrets Manager     OpenAI API      CloudWatch Logs
        │
        ▼
 AI Log Analysis
        │
        ▼
 Amazon SNS
        │
        ▼
 Email Notification
```

---

# ⚙️ Workflow

1. User uploads a log file to Amazon S3.

2. Amazon S3 automatically triggers AWS Lambda.

3. Lambda downloads the uploaded log.

4. Lambda retrieves the OpenAI API Key securely from AWS Secrets Manager.

5. The log content is sent to OpenAI.

6. OpenAI generates:

- Executive summary
- Incident analysis
- Security observations
- Recommendations

7. Lambda creates a formatted report.

8. Amazon SNS sends the report by email.

9. CloudWatch stores execution logs.

Everything happens automatically within seconds.

---

# ⭐ Features

| Feature | Description |
|----------|-------------|
| AI Log Analysis | Intelligent log understanding using OpenAI |
| Automatic Processing | S3 event automatically triggers Lambda |
| Secure Secret Storage | API key stored in AWS Secrets Manager |
| Email Alerts | AI report sent using Amazon SNS |
| Cloud Monitoring | CloudWatch execution logs |
| Serverless | No EC2 or server management |
| Event Driven | Uploading a file starts the workflow |
| Security Detection | AI identifies suspicious events |
| Error Detection | Database and application failures detected |
| Infrastructure Monitoring | System health logs analyzed |

---

# 🧠 AI Analysis Pipeline

```

```text
Log File

↓

Amazon S3

↓

AWS Lambda

↓

Secrets Manager
(API Key)

↓

OpenAI GPT

↓

AI Analysis

↓

Professional Report

↓

Amazon SNS

↓

Email Notification
```

The generated report contains:

- Brief Summary
- Major Findings
- Error Detection
- Security Risks
- Recommended Actions
- Severity Assessment

Unlike keyword matching, the AI understands the overall meaning of the logs and provides contextual insights.

---
