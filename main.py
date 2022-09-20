from instaloader import Instaloader, Profile

L = Instaloader()
PROFILE = str(input('Write username here: '))
profile = Profile.from_username(L.context, PROFILE)

posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes,reverse=True)

for post in posts_sorted_by_likes:
    if post.is_video:
        L.download_post(post, PROFILE)
