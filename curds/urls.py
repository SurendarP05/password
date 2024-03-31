from  django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('curd', curdViwset)

# curd_list_view = curdViwset.as_view({
#     "get" :"list",
#     "post" : "create",
#     "delete":"destroy"
  

# })

urlpatterns=[
    #    path('curd/', include(router.urls)),
    #    path('create/',CreationDetail.as_view() ,name="create-data"),
        #  path('getinfo/',DetailInfo.as_view() ,name="get-data"),
    #    path ('update/<int:id>',UpdateDetail.as_view(),name="update-data"),
    #    path('delete/<int:id>',DeleteDetail.as_view(),name="delete-data"),
    #    path('retrive/<int:pk>',RetriveData.as_view()),
         path('create/',CurdListView.as_view()),
    #    path('generic/curd/<int:id>',curd_list_view)
         path('delete/',CurdDestroyListView.as_view()),
         path('delete/<int:id>',CurdDestroyListView.as_view(),name="delete-data"),
]