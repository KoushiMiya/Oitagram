from django.urls import path
from . import views

#URLパターンを逆引きできるように名前を付ける
app_name = 'photo'

#URLパターンを登録する変数
urlpatterns = [
    #photoアプリへのアクセスはviewモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),

    #p446で追加
    #写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('post/', views.CreatePhotoView.as_view(), name='post'),

    #p450で追加
    #投稿完了ページへのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),
    
    # カテゴリ一覧ページ
    # photos/<Categorysテーブルのid値>にマッチング
    # <int:category>は辞書{category: id(int)}としてCategoryViewに渡される
    path('photos/<int:category>',
         views.CategoryView.as_view(),
         name = 'photos_cat'
        ),
    
    path('user-list/<int:user>',
        views.UserView.as_view(),
        name = 'user_list'
        ),

    #詳細ページ
    #photo-detail/<Photo Postsテーブルのid値>にマッチング
    #<int:pk>は辞書{pk: id(int)}としてDetailViewに渡される
    path('photo-detail/<int:pk>',
         views.DetailView.as_view(),
         name = 'photo_detail'
        ),
    
    # マイページ
    # mypage/へのアクセスはmypageViwを実行
    path('mypage/', views.MypageView.as_view(), name = 'mypage'),

    #URLを登録する変数

    #投稿写真の削除
    #photo/<Photo postsテーブルのid値>/delete/にマッチング
    #<int:pk>は{pk: id(int)}としてDetailViewに渡される
    path('photo/<int:pk>/delete/',
         views.PhotoDeleteView.as_view(),
         name = 'photo_delete'
        ),
]