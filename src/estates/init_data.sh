#!/bin/sh
#
# Script to generate initial data to satisfy the assignment requirements.
#
# NOTES
# - Use soft tabs, not \t
# - User password: "pass"

USERS=5
MIN_PLACE=5
MAX_PLACE=30
CATEGORIES=3

echo "#"
echo "# Initial Users"
echo "#"

for i in `jot - 2 $USERS`; do
    echo '- model: auth.user'
    echo "  pk: $i"
    echo '  fields:'
    echo "    date_joined: 2010-01-01 01:01:01.000000"
    echo "    email: user$i@example.com"
    echo "    is_active: true"
    echo "    is_staff: false"
    echo "    is_superuser: false"
    echo "    last_login: 2010-01-01 01:01:01.000000"
    echo '    password: sha1$06c12$67aa4cc0f2e1ca5dc19fcc64af6a5a0e5052d8cb'
    echo "    username: user$i"
    echo
done


echo "#"
echo "# Sample places"
echo "#"

places=0
for i in `jot - 1 $USERS`; do
  USER_PLACES=`jot -r 1 $MIN_PLACE $MAX_PLACE`
  for each in `jot - 1 $USER_PLACES`; do
    let places+=1 > /dev/null
    rand=`jot -r 1 1 37`
    place=`sed -n ${rand}s/,\ /,/gp addresses`
    echo "- model: places.Place"
    echo "  pk: $places"
    echo "  fields:"
    echo "    address     : \"`echo $place | cut -d, -f1`\""
    echo "    zipcode     : `jot -r 1 22221 27482`"
    echo "    city        : \"Πάτρα\"" 
    echo "    country     : \"Ελλάδα\""
    echo "    latitude    : \"`echo $place | cut -d, -f2`\""
    echo "    longitude   : \"`echo $place | cut -d, -f3`\""
    echo 
    echo "    submitter: $i"
    echo "    action: 'S'"
    echo "    price: `jot -r 1 300 1550`"
    echo "    area: `jot -r 1 30 230`"
    echo "    year: `jot -r 1 1965 2009`"
    echo "    description: \"Place $each of user$i\""
    echo
    echo "    category: `jot -r 1 1 $CATEGORIES`"
    echo "    pub_date: 2010-01-01 02:02:02.000000"
    echo "    published: True"
    echo
  done
done

echo "#"
echo "# Some photos"
echo "#"

for i in `jot - 2 $USERS`; do
    echo '- model: places.photo'
    echo "  pk: 1"
    echo '  fields:'
    echo "    pic: uploads/ivPXM_1.jpg"
    echo "    place: 1"
    echo
done
