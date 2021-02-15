Photo classifier
================

Just a fun script to try out the Google Vision API. Thanks to @jmgibson71 for the code
and inspiration. Just a note that using this API costs money. I currently have free
credits that expire soon, but @jmgibson71 noted that it costs about $30 to label about
15,000 photos.


google setup
------------

1. Login to your Google cloud account and create credentials for Vision API, which will
   download a credentials.json file to your computer. Copy that to this directory::

     cp ~/Downloads/vkurup-ckad-5033a83c8926.json my-vision-creds.json

#. Add a reference to that file to your environment variables::

     export GOOGLE_APPLICATION_CREDENTIALS="my-vision-creds.json"

#. Install the `gcloud tool <https://cloud.google.com/sdk/docs/install>`_

#. Confirm that your authentication works::

     gcloud auth application-default print-access-token


setup
-----

1. Create a virtualenv

#. Set your ``PHOTOS_DIR`` env var where this app will look for your photos (can be nested
   in folders)::

     export PHOTOS_DIR=/home/vkurup/Pictures

#. Install requirements::

     pip install -U pip wheel
     pip install -Ur requirements.txt

#. Run the tool::

     python label_maker.py

   It will print out status on the console and you can find logs about only the photos
   it thinks are potentially documents in the ``logs`` directory.
