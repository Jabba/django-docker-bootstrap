#!/bin/bash

# Setup setup mail account
DEFAULT_FROM_EMAIL='noreply@domain.tld'
EMAIL_HOST_USER='user1@domain.tld'
EMAIL_HOST_PASSWORD='mypassword'

mkdir -p config
touch config/postfix-accounts.cf

echo $DEFAULT_FROM_EMAIL > config/default_from_email.txt
echo $EMAIL_HOST_USER > config/email_host_user.txt
echo $EMAIL_HOST_PASSWORD > config/email_host_password.txt

docker run --rm \
  -e MAIL_USER=$EMAIL_HOST_USER  \
  -e MAIL_PASS=$EMAIL_HOST_PASSWORD \
  -ti tvial/docker-mailserver:latest \
  /bin/sh -c 'echo "$MAIL_USER|$(doveadm pw -s SHA512-CRYPT -u $MAIL_USER -p $MAIL_PASS)"' >> config/postfix-accounts.cf

# Generate DKIM keys
docker run --rm \
  -v "$(pwd)/config":/tmp/docker-mailserver \
  -ti tvial/docker-mailserver:latest generate-dkim-config
