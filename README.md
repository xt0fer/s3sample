# S3 simple

load a file with your name in it to a S3 bucket.

be sure to get the current creds from the instructor.

## Steps

* create a file named after yourself. 
* put your name in the file.
* edit the script(s) to
  * use your github handle/name instead of None
* be sure the creds are in the environment variables of your terminal's shell
* run the script to upload your file into your "namespace"
* make sure you have the AWS CLI downloaded
* make sure you have setup the credentials in the ~/.aws directory
* perform a `aws s3 ls` command on your directory inside of the bucket
* so it might be something like `aws s3 ls bucketname/students/yourgithub/`
  * and you should see the file you uploaded

