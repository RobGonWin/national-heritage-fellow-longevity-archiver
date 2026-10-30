"""Build only the reviewed public site and publication files; no repository walk."""
from pathlib import Path
import shutil
from public_offline import validate
def build(root=Path(__file__).resolve().parent):
    validate(root/'data/public')
    root=root.resolve();out=root/'build'
    if out.is_symlink() or out.resolve().parent!=root:
        raise ValueError('Build destination must remain under the project root')
    if out.exists():shutil.rmtree(out)
    out.mkdir()
    for source,target in [('site','site'),('data/public','data/public')]:
        shutil.copytree(root/source,out/target,dirs_exist_ok=True)
    (out/'docs').mkdir(exist_ok=True)
    for name in ('image-source-register.json','source-link-audit.json'):
        shutil.copyfile(root/'docs'/name,out/'docs'/name)
    (out/'index.html').write_text('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=site/"><a href="site/">Open the archival comparison</a>',encoding='utf-8')
    (out/'.nojekyll').touch()
    print('Validated static site: '+str(out))
if __name__=='__main__':build()
