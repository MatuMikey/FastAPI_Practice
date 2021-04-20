import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get('/')
@template()
def index():
    return {
        'package_count': 274_800,
        'release_count': 2_234_847,
        'user_count': 73_874,
        'packages': [
            {'id': 'fastapi', 'summary': "A great web framework"},
            {'id': 'uvicorn', 'summary': "Your favourite ASGI server"},
            {'id': 'https', 'summary': "Requests for an async world"}
        ]
    }


@router.get('/about')
@template(template_file='home/about.pt')
def about():
    return {}
