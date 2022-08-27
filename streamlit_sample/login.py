import streamlit_authenticator as stauth
#https://github.com/mkhorasani/Streamlit-Authenticator

class login:
    def __init__(self) -> None:
        # パスワードをハッシュ化。 リスト等、イテラブルなオブジェクトである必要がある
        # 入力フォームに入力された値と合致するか確認される
        self.hashed_passwords = stauth.Hasher(['taro']).generate()
        self.cred = {'usernames': {
                    'taro': { #This value is authenticated
                        'email': 't@example.com',
                        'name': '太郎',
                        'password': self.hashed_passwords[0]
                    }
                }
            }
        self.cookie_name = 'sid' 
        self.signature_key = 'ZOWHzBo0e9mdfoAzcRVowJ6ERfda'
        self.expire_days = 5
        self.preauth = {'preauthorized': {
                        'emails': ['a@example.com']
                    }
                }
        # cookie_expiry_daysでクッキーの有効期限を設定可能。認証情報の保持期間を設定でき値を0とするとアクセス毎に認証を要求する
        self.authenticator = stauth.Authenticate(
            self.cred,
            self.cookie_name,
            self.signature_key,
            self.expire_days,
            self.preauth
        )