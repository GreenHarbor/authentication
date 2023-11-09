# SET UP

just /pray

## Endpoints

### Auth

https://x4zrqb3326lopv2ceaaedu6ejq0chzpl.lambda-url.ap-southeast-1.on.aws/

Authorization Bearer Token: Use the access_token from the sign_in endpoint

Response

```json
{
  "success": true,
  "message": "User is authenticated",
  "data": {
    "username": "test_user",
    "email": "zdwong.2021@u.edu.sg",
    "tag": ["urgent", "vegan", "organic", "nearby"]
  }
}
```

### Get all users's details

https://sgeyklyoarjxdrnx7meuyvqfky0foteg.lambda-url.ap-southeast-1.on.aws/

Response

```json
{
  "success": true,
  "data": [
    {
      "username": "test_user",
      "email": "zdwong.2021@u.edu.sg",
      "tag": ["urgent", "vegan", "organic", "nearby"]
    }
  ]
}
```

### Signup

https://6z77r7ngbdmkaxr63ph5gto3mi0mvpzb.lambda-url.ap-southeast-1.on.aws/

Request Body

```json
{
  "username": "test_user",
  "password": "zdwong1234",
  "email": "zdwong.2021@u.edu.sg",
  "tag": ["urgent", "vegan", "organic", "nearby"]
}
```

Response

```json
{
  "success": true,
  "message": "Sign up sucessful",
  "data": null
}
```

### Login

https://j732p6o6pjs74hon6ky3r6hfia0mayts.lambda-url.ap-southeast-1.on.aws/

```json
{
  "username": "test_user",
  "password": "zdwong1234"
}
```

Response:

```json
{
  "success": true,
  "message": "Sign up sucessful",
  "data": {
    "id_token": "eyJraWQiOiJScHByQWo2QlhwT1k5UHRidEhOMkIxb240ZkRDVEFSbDVaaVoyamJldE5vPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJiOGJlODU4My01NGEyLTQ2NzQtOWVmMS01YjIwNTBiMGVkY2EiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV9rQ2xaMGxvZ0kiLCJjb2duaXRvOnVzZXJuYW1lIjoidGVzdF91c2VyIiwib3JpZ2luX2p0aSI6ImRjM2M5YmQ5LTY5MmUtNGJmMC05MTMzLWMzZWY5NTA5NzAzMSIsImF1ZCI6IjVuZWdkamFlZGZtNGhnY3RycXA2dWRuZTM2IiwiZXZlbnRfaWQiOiIwODUxNjM0Ny0zMjEwLTQ4YTEtOTk0OS05ZGQ1OGExNzFmM2QiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY5OTAxOTcyMSwiZXhwIjoxNjk5MDIzMzIxLCJpYXQiOjE2OTkwMTk3MjEsImp0aSI6IjBmNWFlOTQyLWQ1YTYtNGViOC05ZjI1LTczNTBhM2NkNjFjOSIsImVtYWlsIjoiemR3b25nLjIwMjFAdS5lZHUuc2cifQ.JvTKb38cNBOddAi085j60brBGupPwf4qOTwUQajW7F_7EpZn5QXza3SoUFNaXsd-DZaSiahT1Q9xrBWjZ7E6U-vowz8xoHXOFvTlCbmwI4PxAoOicu63KSubegB5lSnopeP_IjiyYkVtybYJSODGWZbZzVvfRWgmkgJ1sxFGhPoAmliWyEGOE1hcEhdZBU1yaJM5G3cdZmM-vDAIRIhGciiWRUTGjq987YNZtwyvR97b3aZz5LIrZZkqAnd-f5Ct3SBwQUgBdkpZUjpw5aNFKBTb8zAUUhwqP2DASriLscaGoDq0Bn1L5rGRmpTjC_Q-em06dZ3_AmIv53uxSpWeYg",
    "refresh_token": "eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.dS4KDcnH7hRoxqLsZRBIMmbfSp1GpFMkIz7G_Zm24ZSCPQZXpKYQn5oIpp7KrkR-8zAGzJ7cg6ZG39MAyRi4nkxBGB1_x_6GACRBhuu1qKDcQ0X9rEMjlKVqM6dKjcV7K048y2lDuavJIsGDo9Dm1jroO_CnFWP8iM1xfKJKjRHKmig6X6NizAK-crC7EEpAMEFThWxC95_yWHNolEba-V6aY2Xf6qyz7BBWFvrpfG-m2zHQFbMIgZ1pCR2B0gM3sMJ3gAw1Y1zc9_HlVRbXTJ7SAyX3pf-kX54KAgk_5Lpuk4V1zyc70ZwsQfqL88TlvJ6Tw3SmNKAdCeuuPH5xdw.hFxY-Vnlpr7ENuHt._O39CordsWBazjcGWNvNr_ehkyQ5EDKDAUCjrwSDnfTUaNfDyGZFz-hBTdaYrSSU6l59qQs6xGhH285OcLJeKVNCsEL04lzU_xt-BRV9qiyWkqc0i1ImBSeLbj9xUMkwbvz8J46VvsXJwAvUrTgR0OsOJVa6WRtyulql9h_jJ2VmAOBelNUDYEJbleouSFQHxPODWvgBJJj8aqOQMTZKPQKm2IV4I-0Hx9HbLfwQInmuBq_1dlNf6Iw4twqO-UW-Jvi_cc9tng8EvaYQmYp3RwM4LM99zfYNOa06KzRBlYRsjR1y9CrUYY_Cim6ABvjFXqehIhJUUEeGg05HcVb0GyZMctN5UzsXVzS13h5Rc7wXpDdxWR47jGgD8c-2Ss9UeZ5a3tkmu6_bRmPk26xFVVhTbFwe508W-RzqzPbEVZEywu2jdOwKDa9daLBh4534IbdPSm0T0yKSeFm8QRHFW6BDqnXD05t_swHe99uGeLvjB90IgUN5QNLkq-TLu3vcHcPuE7s6VrVyt6IFMfXDaP6NiPBO8EOOf1iRDawrAODllwG3uZiBfd84nwQp5VNWJznFY50KCJTW0QESL_K94ZmkTpakyIIUPej5940IB9GsMaH3qrzxZX40eL4uEAAV0cpcUzkLL79a1_yNQzdh60DqXdcurjeTYi7NFEBNN_GWrQcClknxI_2Itz4p2Vui8C_mHyMh3qcMpLl_13z7yLWnqST9Rno07Apb2DQYLnJZ-ZKFW5NzfVFkw_fZO_wfit2vZ0THl_EPMRWio9887CNmVpwEssElEfqfIbF80Fv1RPtNHyxCN50cGOsF4msf_CYnM304KME2UCOd296IqDuYPXAuz2AKZqiGKUZI3lPsywCgxvTeluCFBeEt1tPSVBSkyyXYSEDgRafRnw0PglaLOuM76dj6Cvs-hn8uS6Z4A3EM3HabULzbEyjgwCCr8026XLXoWYz-C64Y2PjtxybpNgGTV1fPF7OWzefL_JD67eGoECiT_MYX6svEpgpUFaPvQUPxAT7ctsbpeb8AkgT5CmFdrx5aFWlC0oDJaQrw8oRMbrkx2p_qiR9Ul05YZPABxZZIWJq8Dyt8Ldhs6joQzl8uj059jIsGwg_vfoNUdK2mXNoVq6BoPYkJLqy5Q3vV_o64ntrMWLl0iAa1qkRDJsKboZ5wSNsaO_jW9-HoLNL9Yqscw0FoEKfQPF-iunnukk2TIX0-diKeBUZFWox250ggXh-QEBw1andETTkUe_zLGL9xBPbvhx3SDZKHkNDop3nBovF9h2NP2mS_XgbJGXpY.bkN9DPBc3Tr0cH861hnYzg",
    "access_token": "eyJraWQiOiJKNDZBNnR1d0lWSTRWcnV2K05tK1dsSWc3QzVMVDlHZUFRdGQrTm45V0FFPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJiOGJlODU4My01NGEyLTQ2NzQtOWVmMS01YjIwNTBiMGVkY2EiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTFfa0NsWjBsb2dJIiwiY2xpZW50X2lkIjoiNW5lZ2RqYWVkZm00aGdjdHJxcDZ1ZG5lMzYiLCJvcmlnaW5fanRpIjoiZGMzYzliZDktNjkyZS00YmYwLTkxMzMtYzNlZjk1MDk3MDMxIiwiZXZlbnRfaWQiOiIwODUxNjM0Ny0zMjEwLTQ4YTEtOTk0OS05ZGQ1OGExNzFmM2QiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjk5MDE5NzIxLCJleHAiOjE2OTkwMjMzMjEsImlhdCI6MTY5OTAxOTcyMSwianRpIjoiN2FmNjhhNWItNzZhNi00NzAyLWJiM2ItYWY4NmVhMzhjNGQyIiwidXNlcm5hbWUiOiJ0ZXN0X3VzZXIifQ.DrlxpLSDEGmxYtEc4P_vLzWEtxnIOkhQe3U3yaayCJ63YtaXqKMklGH7VI_BXyQBLYlaHv_MGEebp2vCw2PlycBfVAcgQJaNskQJpXAMMan1JplD--q_y7hBg6zM4LENG5VwnAZ49uMzGXGA9q8hz7cjUt9PhfShLItrcEshr6NU5g7kGIDxLoZ2-yHxTEHsZV_ez2va0zXMhR6gWeOFzzc8vlaATp5TVk9j8hRtwjHmYkx-bxR7RV1U3urCqEkVvzafy9141SQwDy3N_C-cY4RQCnuulJq41kR466Z3CsSMR6KMEHyS8cYMVIOmwubU6G3f5mA9wxRjyek9J9ty_g",
    "expires_in": 3600,
    "token_type": "Bearer"
  }
}
```

```

```
