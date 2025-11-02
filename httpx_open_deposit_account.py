import httpx
import time

BASE_URL = "http://localhost:8003/api/v1"
TIMEOUT = 30

#Создание пользователя с уникальным email
email = f"user{int(time.time())}@example.com"
create_user_payload = {
    "email": email,
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_response = httpx.post(f"{BASE_URL}/users", json=create_user_payload, timeout=TIMEOUT)
assert create_response.status_code == 200, f"Unexpected status: {create_response.status_code}, body: {create_response.text}"
create_data = create_response.json()
user_id = create_data["user"]["id"]

# Пауза, чтобы данные точно были доступны дальше
time.sleep(0.5)

# Открытие депозитного счёта для созданного пользователя
open_deposit_payload = {"userId": user_id}
open_response = httpx.post(f"{BASE_URL}/accounts/open-deposit-account", json=open_deposit_payload, timeout=TIMEOUT)

assert open_response.status_code == 200, f"Unexpected status: {open_response.status_code}, body: {open_response.text}"
open_data = open_response.json()


print("Open deposit account response:", open_data)
print("Status Code:", open_response.status_code)