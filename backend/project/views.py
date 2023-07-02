# Create your views here.
from rest_framework.response import Response
from  rest_framework.decorators import  api_view
from .models import *
from .serializers import *
from rest_framework.status import *
from django.shortcuts import  get_object_or_404
# from rest_framework.permissions import  IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
# from rest_framework import permissions,authentication
# from rest_framework.decorators import permission_classes
from . import github
@api_view(['DELETE'])
def DeleteProject(req,id):
    data=get_object_or_404(Project,id=id)
    data.delete()
    return Response(status=HTTP_200_OK)



@api_view(['PUT'])
def UpdateProject(request,id):
    updateobject=get_object_or_404(Project,id=id)
        #Project1ser.
    updateobjectafterupdate=Projectselizer(instance=updateobject,data=request.data)
    if(updateobjectafterupdate.is_valid()):
        updateobjectafterupdate.save()
        return Response(status=HTTP_202_ACCEPTED,data=updateobjectafterupdate.data)
    return Response(status=HTTP_406_NOT_ACCEPTABLE,data={"detail":"not valid update data"})

@api_view(['POST'])
def AddProject(request):


    workspace=Workspace.objects.get(id=request.data['workspace_id'])
    if workspace.integrate!=False:
        if  workspace.token==None:
            return Response(status=HTTP_406_NOT_ACCEPTABLE,data={"detail":"please add github token"})
        repo=github.create_repo(request.data['name'],workspace.token)
        request.data['clone_url']=repo[0]
        request.data['repo_name']=repo[1]

    item=Projectselizer(data=request.data)
    
    if(item.is_valid()):
        item.save()
        return  Response(status=HTTP_200_OK ,data=item.data)
    else:
        return  Response(status=HTTP_417_EXPECTATION_FAILED)


@api_view(['GET'])
def ListProject(request,id=None):
    #select all catgory from model
    print(request.user.id)
    print(request.GET.get('workspaceId'))
    if(id is not None):
        data=get_object_or_404(Project,id=id)
        dataserlized=Projectselizer(data)
        return Response(status=HTTP_202_ACCEPTED, data= dataserlized.data)
    else:
        data=Project.objects.all().filter(workspace_id=request.GET.get('workspaceId'))
        dataserlized=Projectselizer(data,many=True)
        return Response(status=HTTP_207_MULTI_STATUS,data= dataserlized.data)


def validate_integration():
    pass
