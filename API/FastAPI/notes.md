git add .
git commit -m "first commit"
git push -u origin main   

curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"name": "orange"}'