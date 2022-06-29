class MyPostListView:
    @signin_required
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        my_post=[post for post in posts if post["userId"]==userId]
        return my_post
myposts=MyPostListView()
print(myposts.get())