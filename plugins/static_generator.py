import os
import shutil
import logging
import pelican
from pelican.utils import copy, process_translations, mkdir_p
from pelican import signals
from pelican.contents import Static
from pelican.generators import StaticGenerator
#from pelican.readers import read_file

import pdb

logger = logging.getLogger(__name__)

class AllStaticGenerator(StaticGenerator):
    """
    Take over for the real static generator and just implement what we want
    """
    def generate_context(self):
        if not hasattr(self, "staticfiles"):
            self.staticfiles = self.context["staticfiles"]

        # walk static paths
        # for static_path in self.settings['STATIC_PATHS']:
        #     for f in self.get_files(
        #             static_path, extensions=False):

        for dirpath, dirnames, filenames in os.walk(self.path):
            for f in filenames:

                full_path = os.path.join(dirpath, f)
                fname, fext = os.path.splitext(full_path)

                skip = False
                if fext in ('.rst','.md'):
                    continue

                if 'theme' in f:
                    #print("NO: ", f)
                    continue

                for source,destination in self.settings['FILES_TO_COPY']:
                    if f == source:
                        skip = True
                        break

                for source,destination in self.settings['TEMPLATE_PAGES'].items():
                    if f == source:
                        skip = True
                        break

                if f.startswith(self.settings['THEME']):
                    continue

                if skip:
                    continue


                static = self.readers.read_file(
                    base_path=self.path, path=full_path, content_class=Static,
                    fmt='static', context=self.context,
                    preread_signal=signals.static_generator_preread,
                    preread_sender=self,
                    context_signal=signals.static_generator_context,
                    context_sender=self)
                self.staticfiles.append(static)
                self.add_source_path(static)

        # pdb.set_trace()
        # print self.staticfiles
        self._update_context(('staticfiles',))
        # print self.context

    def generate_output(self, writer):
        # copy all Static files
        # pdb.set_trace()
        for sc in self.context['staticfiles']:
            source_path = os.path.join(self.path, sc.source_path)
            save_as = os.path.join(self.output_path, sc.save_as)
            mkdir_p(os.path.dirname(save_as))
            shutil.copy(source_path, save_as)
            logger.info('copying {} to {}'.format(sc.source_path, sc.save_as))

    # def generate_context(self):
    #     print "GENERATING CONTEXT"
    #     ret = StaticGenerator.generate_context(self)
    #     # self.staticfiles = []
    #     # walk static paths
    #     for dirpath, dirnames, filenames in os.walk(self.path):
    #         print filenames
    #         for f in filenames:
    #             full_path = os.path.join(dirpath, f)
    #             fname, fext = os.path.splitext(full_path)

    #             skip = False
    #             if fext in ('.rst','.md'):
    #                 continue

    #             if 'theme' in f:
    #                 print "NO: ", f
    #                 continue

    #             for source,destination in self.settings['FILES_TO_COPY']:
    #                 if f == source:
    #                     skip = True
    #                     break

    #             for source,destination in self.settings['TEMPLATE_PAGES'].items():
    #                 if f == source:
    #                     skip = True
    #                     break

    #             if f.startswith(self.settings['THEME']):
    #                 continue

    #             if skip:
    #                 continue

    #             static = self.readers.read_file(
    #                 base_path=self.path, path=full_path, content_class=Static,
    #                 fmt='static', context=self.context,
    #                 preread_signal=signals.static_generator_preread,
    #                 preread_sender=self,
    #                 context_signal=signals.static_generator_context,
    #                 context_sender=self)
    #             print static
    #             self.staticfiles.append(static)
    #             self.add_source_path(static)
    #     self._update_context(('staticfiles',))
    #     return ret






##################

    # """Copy static files from content folder.
    # Ignores .md and .rst files and copies everything else to output dir.
    # Raises exception when file from another directory could be overwritten.
    # """

    # def _copy_paths(self, paths, source, destination, output_path,
    #         final_path=None):
    #     """Copy all the paths from source to destination"""
    #     for path in paths:
    #         copy(path, source, os.path.join(output_path, destination),
    #              final_path, overwrite=True)

    # def in_staticfiles(self, f):
    #     for sc in self.staticfiles:
    #         if os.path.join(self.output_path, f) == sc.save_as:
    #             return True
    #     return False

    # def generate_context(self):
    #     self.staticfiles = []

    #     # self.path - content folder path
    #     # walk static paths
    #     for dirpath, dirnames, filenames in os.walk(self.path):
    #         for f in filenames:
    #             import pdb
    #             pdb.set_trace()

    #             full_path = os.path.join(dirpath, f)
    #             fname, fext = os.path.splitext(full_path)

    #             skip = False
    #             if fext in ('.rst','.md'):
    #                 continue

    #             for source,destination in self.settings['FILES_TO_COPY']:
    #                 if f == source:
    #                     skip = True
    #                     break

    #             for source,destination in self.settings['TEMPLATE_PAGES'].items():
    #                 if f == source:
    #                     skip = True
    #                     break

    #             if skip:
    #                 continue

    #             #considering every non-content file as static file
    #             f_rel = os.path.relpath(full_path, self.path)
    #             f_basename = os.path.basename(f_rel)

    #             if f_rel.startswith('pages'):
    #                 dest = os.path.join('pages', f_basename)
    #             else:
    #                 dest = f_basename

    #             if self.in_staticfiles(dest):

    #                 raise Exception("%s already exists in output path. Tried to copy: %s" % (f_basename, f_rel))

    #             return
    #             content, metadata = self.readers.read_file(
    #                 f, fmt='static', settings=self.settings)

    #             metadata['save_as'] = os.path.join('output', f_rel)
    #             metadata['url'] = pelican.utils.path_to_url(metadata['save_as'])

    #             sc = Static(
    #                 content=None,
    #                 metadata=metadata,
    #                 settings=self.settings,
    #                 source_path=full_path)


    #             # sc = Static(
    #             #     content=None,
    #             #     metadata=metadata,
    #             #     f_rel, dest, settings=self.settings)
    #             self.staticfiles.append(sc)
    #             self.context['filenames'][f_rel] = sc


    # def generate_output(self, writer):
    #     self._copy_paths(self.settings['THEME_STATIC_PATHS'], self.theme,
    #                      'theme', self.output_path, '.')
    #     # copy all StaticContent files
    #     for sc in self.staticfiles:
    #         mkdir_p(os.path.dirname(sc.save_as))
    #         shutil.copy(sc.source_path, sc.save_as)
    #         logger.info('copying %s to %s' % (sc.source_path, sc.save_as))



def return_generator(sender):
    return AllStaticGenerator

def register():
    signals.get_generators.connect(return_generator)

