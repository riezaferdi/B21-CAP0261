from googleapiclient.discovery import build
gcs_service = build('storage', 'v1')

from googleapiclient.http import MediaFileUpload
def upload_file(filename, filetype, bucket_name, loc):
    media = MediaFileUpload(filename,
                            mimetype=filetype,
                            resumable=True)

    request = gcs_service.objects().insert(bucket=bucket_name,
                                           name=loc,
                                           media_body=media)

    response = None
    while response is None:
      # _ is a placeholder for a progress object that we ignore.
      # (Our file is small, so we skip reporting progress.)
      _, response = request.next_chunk()

    print('Upload complete')


from apiclient.http import MediaIoBaseDownload
def download_file(filename, bucket_name, loc):
    with open(filename, 'wb') as f:
      request = gcs_service.objects().get_media(bucket=bucket_name,
                                                object=loc)
      media = MediaIoBaseDownload(f, request)

      done = False
      while not done:
        # _ is a placeholder for a progress object that we ignore.
        # (Our file is small, so we skip reporting progress.)
        _, done = media.next_chunk()

    print('Download complete')


