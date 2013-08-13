import os
import shutil
import logging
import pelican
from pelican.utils import copy, process_translations, mkdir_p
from pelican import signals
from pelican.contents import Static
from pelican.generators import Generator
from pelican.readers import read_file

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
        # pdb.set_trace()

        # self.path - content folder path
        # walk static paths
        for dirpath, dirnames, filenames in os.walk(self.path):
            for f in filenames:
                full_path = os.path.join(dirpath, f)
                fname, fext = os.path.splitext(full_path)

                skip = False
                if fext in ('.rst','.md'):
                    continue

                for source,destination in self.settings['FILES_TO_COPY']:
                    print f, source
                    if f == source:
                        skip = True
                        break

                if skip:
                    continue

                #considering every non-content file as static file
                f_rel = os.path.relpath(full_path, self.path)
                f_basename = os.path.basename(f_rel)
                print f_rel
                if f_rel.startswith('pages'):
                    dest = os.path.join('pages', f_basename)
                else:
                    dest = f_basename

                if self.in_staticfiles(dest):

                    raise Exception("%s already exists in output path. Tried to copy: %s" % (f_basename, f_rel))

                content, metadata = read_file(
                    f, fmt='static', settings=self.settings)

                metadata['save_as'] = os.path.join('output', f_rel)
                metadata['url'] = pelican.utils.path_to_url(metadata['save_as'])

                sc = Static(
                    content=None,
                    metadata=metadata,
                    settings=self.settings,
                    source_path=full_path)


                # sc = Static(
                #     content=None,
                #     metadata=metadata,
                #     f_rel, dest, settings=self.settings)
                self.staticfiles.append(sc)
                self.context['filenames'][f_rel] = sc


    def generate_output(self, writer):
        self._copy_paths(self.settings['THEME_STATIC_PATHS'], self.theme,
                         'theme', self.output_path, '.')
        # copy all StaticContent files
        for sc in self.staticfiles:
            mkdir_p(os.path.dirname(sc.save_as))
            shutil.copy(sc.source_path, sc.save_as)
            logger.info('copying %s to %s' % (sc.source_path, sc.save_as))



def return_generator(sender):
    return StaticGenerator

def register():
    signals.get_generators.connect(return_generator)

