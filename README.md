# 🤖 AI Log Analyzer on AWS

> Production-ready serverless AI Log Analyzer built with **AWS Lambda, Amazon S3, Amazon SNS, CloudWatch, IAM, Secrets Manager, and OpenAI GPT**.

Automatically detects errors inside uploaded log files, generates an AI-powered analysis report, stores the report in Amazon S3, and sends the result via email using Amazon SNS.

---

# 🚀 Project Overview

This project demonstrates a complete serverless AI pipeline on AWS.

Instead of manually reading thousands of log lines, the application automatically:

- Uploads log files
- Triggers AWS Lambda
- Reads log contents
- Sends logs to OpenAI GPT
- Generates an intelligent analysis
- Stores the report in Amazon S3
- Emails the final report to the administrator

Everything is fully automated.

---

# 🏗 Architecture

```
              Sample Log File
                     │
                     ▼
            Amazon S3 Bucket
                     │
      Object Created Event Trigger
                     │
                     ▼
          AWS Lambda (Python 3.12)
                     │
     ┌───────────────┼────────────────┐
     │               │                │
     ▼               ▼                ▼
OpenAI API     Secrets Manager   CloudWatch
     │
     ▼
AI Analysis Report
     │
     ▼
Amazon S3 (Reports)
     │
     ▼
Amazon SNS
     │
     ▼
Email Notification
```

---

## 📷 Architecture Diagram

![Architecture](images/Architecture-Overview.png)

---

# ✨ Key Features

- AI-powered log analysis using OpenAI GPT
- Fully serverless AWS architecture
- Automatic Lambda trigger from S3 upload
- Secure API key storage using Secrets Manager
- CloudWatch monitoring
- Email notifications through SNS
- AI-generated incident reports
- Production-style IAM permissions
- Sample logs included for testing

---

# 🛠 AWS Services Used

| Service | Purpose |
|----------|----------|
| AWS Lambda | Process uploaded logs |
| Amazon S3 | Store logs and AI reports |
| Amazon SNS | Email notification |
| CloudWatch | Monitoring & logging |
| IAM | Secure permissions |
| Secrets Manager | Store OpenAI API Key |

---

# 🧠 AI Workflow

1. Upload a log file into S3.
2. S3 triggers Lambda automatically.
3. Lambda downloads the log.
4. Lambda retrieves the OpenAI API key from Secrets Manager.
5. OpenAI analyzes the log.
6. AI report is generated.
7. Report is uploaded to S3.
8. SNS sends an email with the analysis result.

---

# 📸 Project Screenshots

---

## 💻 Lambda Function

Core Python function that processes uploaded logs and communicates with OpenAI.

![Lambda Code](images/lambda-code.png)

---

## 🔐 AWS Secrets Manager

The OpenAI API Key is securely stored inside AWS Secrets Manager instead of hardcoding sensitive information into the application.

![Secrets Manager](images/aws-secrets-manager.png)

---

## 👤 IAM Role & Permissions

AWS IAM provides secure access between S3, Lambda, Secrets Manager, CloudWatch, and SNS using least-privilege permissions.

![IAM](images/iam-role-permissions.png)

---

## 📊 CloudWatch Monitoring

CloudWatch captures execution logs for every Lambda invocation, enabling monitoring, debugging, and auditing.

![CloudWatch](images/cloudwatch-execution-logs.png)

---

## 📧 Amazon SNS Email Subscription

Amazon SNS delivers AI-generated reports directly to the registered email address.

![SNS](images/sns-email-subscription.png)

---

## 📨 AI Log Analysis Report

Sample email received after successful AI analysis.

![Email Report](images/email-analysis-report.png)

---
