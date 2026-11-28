# Generate the boto3 client for interacting with S3
from turtle import pd


s3 = boto3.client('s3', region_name='us-east-1', 
                        # Set up AWS credentials 
                        aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)
# List the buckets
buckets = s3.list_buckets()

#output
# {'Buckets': [{'Name': 'gim-staging', 'CreationDate': datetime.datetime(2023, 1, 1, 0, 0, 0, tzinfo=tzutc())}]}


# Create a new bucket
bucket = s3.create_bucket(Bucket='gim-staging')


#delete the bucket
s3.delete_bucket(Bucket='gim-test')


# Print the buckets
print(buckets)


#upload a file to the bucket
s3.upload_file(Filename='local_file.txt', Bucket='gim-staging', Key='remote_file.txt')

#view the contents of the bucket
objects = s3.list_objects(Bucket='gim-staging')

#view single object
object = s3.get_object(Bucket='gim-staging', Key='remote_file.txt')
#return dict with metadata and body of the object
#for example, 
#[{Key: 'remote_file.txt', 'LastModified': datetime.datetime(2023, 1, 1, 0, 0, 0, tzinfo=tzutc()), 'ETag': '"d41d8cd98f00b204e9800998ecf8427e"', 'Size': 0, 'StorageClass': 'STANDARD'}]
object = s3.get_head_object(Bucket='gim-staging', Key='remote_file.txt')  #show the metadata of the object


#deleting sorted objects# List only objects that start with '2018/final_'
response = s3.list_objects(Bucket='gid-staging', 
                           Prefix='2018/final_')

# Iterate over the objects
if 'Contents' in response:
  for obj in response['Contents']:
      # Delete the object
      s3.delete_object(Bucket='bucket_name', Key=obj['Key'])

# Print the keys of remaining objects in the bucket
response = s3.list_objects(Bucket='gid-staging')

for obj in response['Contents']:
  	print(obj['Key'])
   
#uploading with access control
# Upload the final_report.csv to gid-staging bucket
s3.upload_file(
  # Complete the filename
  Filename='./final_report.csv', 
  # Set the key and bucket
  Key='2019/final_report_2019_02_20.csv', 
  Bucket='gid-staging',
  # During upload, set ACL to public-read
  ExtraArgs = {
    'ACL': 'public-read'})

#download and share private files
# Generate presigned_url for the uploaded object
share_url = s3.generate_presigned_url(
  # Specify allowable operations
    = 'get_object',
  # Set the expiration time
  ____=____,
  # Set bucket and shareable object's name
  ____={'Bucket': '____','Key': '____'}
)

# Print out the presigned URL
print(____)

#saving to a dataframe
df_list = []

for file in response['Contents']:
  # For each file in response load the object from S3
  obj = s3.get_object(Bucket='gid-requests', Key=file['Key'])
  # Load the object's StreamingBody with pandas
  obj_df = pd.read_csv(obj['Body'])
  # Append the resulting DataFrame to list
  df_list.append(obj_df)

# Concat all the DataFrames with pandas
df = pd.concat(df_list)

# Preview the resulting DataFrame
df.head()
  