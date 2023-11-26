import asyncio
import inspect


def asyncio_run(async_func):

    def wrapper(*args, **kwargs):
        return asyncio.run(async_func(*args, **kwargs))
    
    wrapper.__signature__ = inspect.signature(async_func)  # without this, fixtures are not injected

    return wrapper


@asyncio_run
async def test_get_file_list(d_service):
    files = await d_service.get_file_list('')
    print(files)

