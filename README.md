# AWS Static Website Project

I created a static website of my resume using Amazon S3, and then distributed it globally via CloudFront. I then created a custom DNS domain name in Route 53, which I pointed to the CloudFront distribution. To gain insights into website traffic, I enabled CloudFront access logging, then used AWS Glue and Amazon Athena to catalog and query the log data stored in S3. This project demonstrates both front-end hosting and back-end data analysis, and is part of my cloud portfolio as I begin my cloud journey.

To track visitors in real-time, I added a backend pipeline:

- Created an AWS Lambda function to log visitor info — including IP, timestamp, browser, and page visited.
- Exposed the Lambda through API Gateway so it could be triggered from the website.
- Set up Amazon Kinesis Data Firehose to take those logs from Lambda and store them in S3.
- Tested the full flow: site visit → API Gateway → Lambda → Firehose → S3.

# Services Used

- Amazon S3 (static site hosting)
- AWS CloudFront (CDN distribution)
- AWS Glue (data catalog and crawler)
- Amazon Athena (serverless query engine)
- Amazon Route 53 (DNS)
- AWS Lambda (visitor logging)
- Amazon API Gateway (HTTP endpoint)
- Amazon Kinesis Data Firehose (real-time delivery to S3)

# How I Deployed

1. Uploaded static files (HTML/CSS/JS) to an S3 bucket.
2. Enabled static website hosting on the bucket.
3. Set up a CloudFront distribution pointing to the S3 origin.
4. Created a custom DNS domain in Route 53 and routed it to the CloudFront distribution.
5. Enabled CloudFront access logs and configured them to be delivered to a folder in the S3 bucket.
6. Created an AWS Glue crawler to scan and catalog the CloudFront log data in S3.
7. Created a Glue database to store the metadata from the crawler.
8. Queried the log data using Amazon Athena to analyze traffic, most visited pages, and client IPs.
9. Built a Lambda function to log visitor information (IP, timestamp, browser, page path) in real-time.
10. Set up an API Gateway endpoint to trigger the Lambda function from the website.
11. Configured Amazon Kinesis Data Firehose to deliver the visitor logs from Lambda to S3 automatically.
12. Tested the full workflow to ensure site visits trigger Lambda and store records in S3


# Link to Website
stefanfarianresume.com

## Screenshots
<img width="1456" alt="Screenshot 2025-06-27 at 2 54 40 PM" src="https://github.com/user-attachments/assets/49d40c0b-88f5-494b-b31a-406304996caa" />
<img width="741" height="520" alt="Screenshot 2025-07-22 at 9 03 53 PM" src="https://github.com/user-attachments/assets/3a55ff52-fc08-4418-8387-b41ddd498c97" />
<img width="1321" alt="Screenshot 2025-06-27 at 3 01 22 PM" src="https://github.com/user-attachments/assets/b68d33b3-7a41-42e0-86ef-87b125fe733e" />
<img width="1603" height="417" alt="Screenshot 2025-07-28 at 3 37 38 PM" src="https://github.com/user-attachments/assets/a60356d7-702a-49f2-9fd9-c0a41d802d33" />
<img width="1894" height="781" alt="Screenshot 2025-07-28 at 3 37 57 PM" src="https://github.com/user-attachments/assets/a84889ea-05ad-42c3-bd69-a370294a7e03" />
<img width="611" height="840" alt="Screenshot 2025-08-23 at 1 25 01 PM" src="https://github.com/user-attachments/assets/92c1d975-477f-43e2-a96e-2dcb633fae44" />
<img width="672" height="797" alt="Screenshot 2025-08-23 at 1 29 39 PM" src="https://github.com/user-attachments/assets/19959543-fd7f-45b6-a751-ee6aaeb6fdaf" />
<img width="1408" height="496" alt="Screenshot 2025-08-23 at 1 26 18 PM" src="https://github.com/user-attachments/assets/b1fedeee-cc5b-43be-8733-ff4b94cf3817" />
<img width="1429" height="491" alt="Screenshot 2025-08-23 at 1 30 08 PM" src="https://github.com/user-attachments/assets/31d431d5-9a1a-4147-a28b-a22daf9412e8" />
