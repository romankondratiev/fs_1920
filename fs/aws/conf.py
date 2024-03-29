import datetime


AWS_GROUP_NAME = 'EnvisionGroup'
AWS_USERNAME = 'fs'
AWS_ACCESS_KEY_ID = 'AKIA2R5PIZK6A2FMH5RS'
AWS_SECRET_ACCESS_KEY = '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'
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True #maybe false?


DEFAULT_FILE_STORAGE = 'fs.aws.utils.MediaRootS3BotoStorage'
FILE_FORM_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'fs.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'fs-bucket'
AWS_BUCKET_NAME = 'fs-bucket'
S3DIRECT_REGION = 'us-east-2'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
FILE_FORM_UPLOAD_DIR = '//%s.s3.amazonaws.com/media/temp_uploads/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = { 
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}