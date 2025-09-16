#!/bin/bash
set -e
BASE="http://localhost:8000"

echo "1. Создаём ключ"
KEY=$(curl -s -X POST "$BASE/auth/token" -d "username=admin&password=admin" | jq -r .access_token)

echo "2. Загружаем PDF с ФИО"
echo "Пациент Иванов И.И., тел. 123-456-7890, дата 01.01.1980" > sample.txt
curl -s -X POST "$BASE/ingest" -H "Authorization: Bearer $KEY" -F "file=@sample.txt" | jq .

echo "3. Ищем"
curl -s "$BASE/ask?q=приёмка" -H "Authorization: Bearer $KEY" | jq .

echo "4. Аудит"
curl -s "$BASE/audit?limit=5" -H "Authorization: Bearer $KEY" | jq .

echo "5. Метрики"
curl -s "$BASE/metrics" | grep -E 'control_tower' || true
