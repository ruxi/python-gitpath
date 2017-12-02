from subprocess import check_output, CalledProcessError
from functools import lru_cache
import os.path


@lru_cache(maxsize=1)
def root(raise_error = False):
    ''' returns the absolute path of the repository root 
    
    raise_error: False (default). If True, will catch error if not a gitpath
    '''
    try:
        base = check_output(['git', 'rev-parse', '--show-toplevel'])
    except CalledProcessError:
        if raise_error:
            raise IOError('Current working directory is not a git repository')
        else:
            print('Current working directory is not a git repository')
            return False
    return base.decode('utf-8').strip()


def abspath(relpath):
    ''' returns the absolute path for a path given relative to the root of
    the git repository
    '''
    return os.path.join(root(), relpath)
