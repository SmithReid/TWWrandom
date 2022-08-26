touch helpers/watch_throughs.txt
echo "\n" >> helpers/watch_throughs.txt
cat helpers/this_time_through.txt >> helpers/watch_throughs.txt
rm helpers/watched.txt
touch helpers/watched.txt
cp helpers/static_watched.txt helpers/watched.txt