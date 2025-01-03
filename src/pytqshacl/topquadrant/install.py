
def get_java():
    import shutil
    path = shutil.which("java")
    return path

class Java:
    def __init__(self, ver='21', jre=True):
        self.ver = ver
        self.jre = jre
        self.install(ver, jre)
    
    def install(self, ver: str, jre: bool):
        if not self.dir():
            import jdk
            print('installing java')
            jdk.install(ver, jre=jre)

    from pathlib import Path
    base = Path.home() / '.jre'
    def dir(self):
        for d in self.base.iterdir():
            if d.is_dir():
                if f'jdk-{self.ver}' in str(d):
                    return d


from ..config import tqshacl_ver as ver
from pathlib import Path
class ShaclInstallation:
    def __init__(self, ver=ver, overwrite=False) -> None:
        _ = Path(__file__).parent / 'src' # could go under java.home
        self.dir = self.download_shacl(ver, _ / f'shacl-{ver}' , overwrite=overwrite)
        gi = (_ / '.gitignore')
        if not gi.exists():
            gi.touch()
            open(gi, 'w').write('*')

        self.ver = ver
        assert(self.home.exists())
        assert(self.logging.exists())
        assert(self.lib.exists())
    

    @staticmethod
    def download_shacl(ver, dir, overwrite=False) -> Path:
        if dir.exists() and not overwrite:
            return dir
        
        import urllib.request
        _ = urllib.request.urlopen(
            ('https://repo1.maven.org/maven2/org/'
             'topbraid/shacl'
             f'/{ver}/shacl-{ver}-bin.zip'))
        _ = _.read()
        from zipfile import ZipFile
        from io import BytesIO
        _ = ZipFile(BytesIO(_))
        _.extractall(dir)
        return dir

    @property
    def home(self) -> Path:
        return self.dir / f"shacl-{self.ver}"
    @property
    def logging(self) -> Path:
        return self.home / "log4j2.properties"
    @property
    def bin(self) -> Path:
        return self.home / 'bin'
    @property
    def lib(self) -> Path:
        return self.home / 'lib'

