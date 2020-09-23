#!/bin/bash


# download the training labels
curl -o data/train_labels.csv https://drivendata-prod.s3.amazonaws.com/data/63/public/train_labels.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARVBOBDCY3EFSLNZR%2F20200923%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200923T215653Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a8bb864c5a486a8fa8ef27d6f92b066eda27935bd98ff05b3a70406b231314e4


# download the training features
curl -o data/train_values.csv https://drivendata-prod.s3.amazonaws.com/data/63/public/train_values.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARVBOBDCY3EFSLNZR%2F20200923%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200923T215653Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a86b00d7f10b8f899ddb5143ce27fe5572d6fbf672f3de66f26ee1ec6c22fc6c


# download submission format
curl -o data/submission_format.csv https://drivendata-prod.s3.amazonaws.com/data/63/public/submission_format_3TFRxH6.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARVBOBDCY3EFSLNZR%2F20200923%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200923T215653Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0eaae47b4503cdc9f41deaf325cfa96d148b1510d62cf185c21e7a79aedcb2e6


# download testing features
curl -o data/test_values.csv https://drivendata-prod.s3.amazonaws.com/data/63/public/test_values.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARVBOBDCY3EFSLNZR%2F20200923%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200923T215653Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=203f25ea731d8dd6a14907a4ed273aa57bbc31905dba6296090fa3ad091dbd3c
