import requests

class TinderAPI:
    def __init__(self, auth_token):
        self.base_url = 'https://api.gotinder.com'
        self.headers = {
            'X-Auth-Token': auth_token,
            'Content-Type': 'application/json'
        }
    
    def get_user_profile(self):
        """Fetch your Tinder profile"""
        url = f'{self.base_url}/v2/profile'
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_recommendations(self):
        """Fetch recommended users"""
        url = f'{self.base_url}/v2/recs/core'
        response = requests.get(url, headers=self.headers)
        return response.json()

    def like_user(self, user_id):
        """Like a user by user_id"""
        url = f'{self.base_url}/like/{user_id}'
        response = requests.get(url, headers=self.headers)
        return response.json()

    def pass_user(self, user_id):
        """Pass (dislike) a user by user_id"""
        url = f'{self.base_url}/pass/{user_id}'
        response = requests.get(url, headers=self.headers)
        return response.json()

# Example usage
if __name__ == "__main__":
    auth_token = 'your_tinder_auth_token_here'  # Replace with your Tinder auth token
    tinder_api = TinderAPI(auth_token)
    
    # Get your profile details
    profile = tinder_api.get_user_profile()
    print(profile)
    
    # Get recommendations
    recommendations = tinder_api.get_recommendations()
    print(recommendations)
    
    # Like the first user in the recommendations
    if recommendations and recommendations.get('data'):
        first_user = recommendations['data']['results'][0]
        user_id = first_user['_id']
        print(f'Liking user: {user_id}')
        response = tinder_api.like_user(user_id)
        print(response)
