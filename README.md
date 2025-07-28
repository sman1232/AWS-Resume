# AWS Static Website Project

I created a static website of my resume using Amazon S3, and then distributed it globally via CloudFront. I then created a custom DNS domain name in Route 53, which I pointed to the CloudFront distribution. This project is part of my cloud portfolio as I begin my cloud journey.

# Services Used

- Amazon S3 (static site hosting)
- AWS CloudFront (CDN distribution)
- AWS Glue (data catalog and crawler)
- Amazon Athena (serverless query engine)
- Amazon Route 53 (DNS)

# How I Deployed

1. Uploaded static files (HTML/CSS/JS) to an S3 bucket.
2. Enabled static website hosting on the bucket.
3. Set up a CloudFront distribution pointing to the S3 origin.
4. Created a custom DNS domain in Route 53 and routed it to the CloudFront distribution.
5. Enabled CloudFront access logs and configured them to be delivered to a folder in the S3 bucket.
6. Created an AWS Glue crawler to scan and catalog the CloudFront log data in S3.
7. Created a Glue database to store the metadata from the crawler.
8. Queried the log data using Amazon Athena to analyze traffic, most visited pages, and client IPs.



# Link to Website
stefanfarianresume.com

## Screenshots
<img width="1456" alt="Screenshot 2025-06-27 at 2 54 40 PM" src="https://github.com/user-attachments/assets/49d40c0b-88f5-494b-b31a-406304996caa" />
<img width="741" height="520" alt="Screenshot 2025-07-22 at 9 03 53 PM" src="https://github.com/user-attachments/assets/3a55ff52-fc08-4418-8387-b41ddd498c97" />
<img width="1321" alt="Screenshot 2025-06-27 at 3 01 22 PM" src="https://github.com/user-attachments/assets/b68d33b3-7a41-42e0-86ef-87b125fe733e" />
<img width="1603" height="417" alt="Screenshot 2025-07-28 at 3 37 38 PM" src="https://github.com/user-attachments/assets/a60356d7-702a-49f2-9fd9-c0a41d802d33" />
<img width="1894" height="781" alt="Screenshot 2025-07-28 at 3 37 57 PM" src="https://github.com/user-attachments/assets/a84889ea-05ad-42c3-bd69-a370294a7e03" />
