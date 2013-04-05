import os
import shutil
import logging

from pelican.utils import copy, process_translations, mkdir_p
from pelican import signals
from pelican.generators import Generator
from pelican.contents import StaticContent



logger = logging.getLogger(__name__)

class StaticGenerator(Generator):
    """Copy static files from content folder.
    Ignores .md and .rst files and copies everything else to output dir.
    Raises exception when file from another directory could be overwritten.
    """

    def _copy_paths(self, paths, source, destination, output_path,
            final_path=None):
        """Copy all the paths from source to destination"""
        for path in paths:
            copy(path, source, os.path.join(output_path, destination),
                 final_path, overwrite=True)

    def in_staticfiles(self, f):
        for sc in self.staticfiles:
            if os.path.join(self.output_path, f) == sc.save_as:
                return True
        return False

    def generate_context(self):
        self.staticfiles = []
        import pdb
        #pdb.set_trace()

        # self.path - content folder path
        # walk static paths
        for dirpath, dirnames, filenames in os.walk(self.path):
            for f in filenames:
                full_path = os.path.join(dirpath, f)
                fname, fext = os.path.splitext(full_path)
                if fext not in ('.rst','.md'):
                    #considering every non-content file as static file
                    f_rel = os.path.relpath(full_path, self.path)
                    f_basename = os.path.basename(f_rel)
                    if f_rel.startswith('pages'):
                        dest = os.path.join('pages', f_basename)
                    else:
                        dest = f_basename

                    if self.in_staticfiles(dest):

                        raise Exception("%s already exists in output path. Tried to copy: %s" % (f_basename, f_rel))

                    

                    sc = StaticContent(f_rel, dest, settings=self.settings)
                    self.staticfiles.append(sc)
                    self.context['filenames'][f_rel] = sc


    def generate_output(self, writer):
        self._copy_paths(self.settings['THEME_STATIC_PATHS'], self.theme,
                         'theme', self.output_path, '.')
        # copy all StaticContent files
        for sc in self.staticfiles:
            mkdir_p(os.path.dirname(sc.save_as))
            shutil.copy(sc.filepath, sc.save_as)
            logger.info('copying %s to %s' % (sc.filepath, sc.save_as))



def return_generator(sender):
    return StaticGenerator

def register():
    signals.get_generators.connect(return_generator)

