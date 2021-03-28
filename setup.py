from setuptools import setup,find_packages
setup(
  name = 'EAMetatrader',         # How you named your package folder (MyLib)
  packages = find_packages(),   # Chose the same as "name"
  version = '1.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Metatrader library for python',   # Give a short description about your library
  author = 'EAScript',                   # Type in your name
  author_email = 'ehsanakbariea8@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/EAScript/EAMT',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/EAScript/EAMT/archive/refs/tags/1.0.2.tar.gz',    # I explain this later on
  keywords = ['EAMetatrader', 'Metatrader', 'Metatrader4', 'Metatrader5', 'python+metatrader', 'MtApi', 'mql4', 'mql5'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pythonnet',
      ],
  include_package_data=True,
  package_data={'EAMetatrader': ['Client/MtApi.dll', 'Client/Newtonsoft.Json.dll', 'Using/System.Drawing.dll', 'Using/WindowsBase.dll']},
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
