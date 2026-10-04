> 노션 원본: https://app.notion.com/p/3ed93f3d109680eb9b9bedd2e5f7cfc7 (마지막 수정 2026-10-02), 2026-10-03 이관

# Authztrace 정탐 오탐 비교표

비공개 메모 목록 조회에 대한 AuthzTrace 판정 결과 (테스트 API, 오탐 vs 정탐)

## 비공개 메모 (Alice & Bob)
```json
ALICE-PRIVATE-MARK
==================
BOB-PRIVATE-MARK
```

# 오탐
```json
[
  {
    "name": "memo_private_list.1: bob -> alice",
    "request": "GET /api/memo?creatorId=1&visibility=PRIVATE",
    "expect": "deny",
    "status": 200,
    "category": "bola",
    "note": "BOLA: 'bob' accessed alice's memo_private_list (1) - HTTP 200"
  },
  {
    "name": "memo_private_list.1: anon -> alice",
    "request": "GET /api/memo?creatorId=1&visibility=PRIVATE",
    "expect": "deny",
    "status": 200,
    "category": "bola",
    "note": "BOLA: 'anon' accessed alice's memo_private_list (1) - HTTP 200"
  },
  {
    "name": "memo_private_list.1: alice -> bob",
    "request": "GET /api/memo?creatorId=2&visibility=PRIVATE",
    "expect": "deny",
    "status": 200,
    "category": "bola",
    "note": "BOLA: 'alice' accessed bob's memo_private_list (2) - HTTP 200"
  },
  {
    "name": "memo_private_list.1: anon -> bob",
    "request": "GET /api/memo?creatorId=2&visibility=PRIVATE",
    "expect": "deny",
    "status": 200,
    "category": "bola",
    "note": "BOLA: 'anon' accessed bob's memo_private_list (2) - HTTP 200"
  }
]
```
⇒ 200 응답이 오면 안 되는 요청이었는데, 200 응답이 되어서 바로 bola로 판정. 하지만 실제로 메모 내용은 유출 되지 않음 (오탐)

# 정탐
```json
[
  {
    "name": "memo_private_list.1: bob -> alice",
    "request": "GET /api/memo?creatorId=1&visibility=PRIVATE",
    "expect": "deny",
    "status": 200,
    "category": "bola",
    "note": "BOLA: 'bob' accessed alice's memo_private_list (1) - HTTP 200; denied response leaked forbidden marker 'ALICE-PRIVATE-MARK'"
  },
  {
    "name": "memo_private_list.1: anon -> alice",
    "request": "GET /api/memo?creatorId=1&visibility=PRIVATE",
    "expect": "deny",
    "status": 200,
    "category": "bola",
    "note": "BOLA: 'anon' accessed alice's memo_private_list (1) - HTTP 200; denied response leaked forbidden marker 'ALICE-PRIVATE-MARK'"
  },
  {
    "name": "memo_private_list.1: alice -> bob",
    "request": "GET /api/memo?creatorId=2&visibility=PRIVATE",
    "expect": "deny",
    "status": 200,
    "category": "bola",
    "note": "BOLA: 'alice' accessed bob's memo_private_list (2) - HTTP 200; denied response leaked forbidden marker 'BOB-PRIVATE-MARK'"
  },
  {
    "name": "memo_private_list.1: anon -> bob",
    "request": "GET /api/memo?creatorId=2&visibility=PRIVATE",
    "expect": "deny",
    "status": 200,
    "category": "bola",
    "note": "BOLA: 'anon' accessed bob's memo_private_list (2) - HTTP 200; denied response leaked forbidden marker 'BOB-PRIVATE-MARK'"
  }
]
```

**차이**

| 항목 | fixed (오탐) | vuln (정탐) |
|---|---|---|
| 상태 코드 | 200 | 200 |
| 판정 | `bola` | `bola` |
| `note`의 표식 누출 문구 | 없음 | 있음 |
| 실제 응답 | 빈 목록 | alice의 비공개 메모 |

⇒ 서버는 제대로 막았는데, 도구가 200을 보고 막지 못한 걸로 잘못 판정
