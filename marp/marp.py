import os
import subprocess
import yaml
import re

from mkdocs.config import base, config_options as c
from mkdocs.plugins import BasePlugin

class MarpConfig(base.Config):
    enabled = c.Type(bool, default=True)
    output_types = c.ListOfItems(c.Choice(['html', 'pdf', 'ppt']), default=['html'])
    output_suffix = c.Type(str, default='_slides')

class Marp(BasePlugin[MarpConfig]):

    def on_post_build(self, config):
        if not self.config['enabled']:
            return

        # Directory where the markdown files are located
        docs_dir = config['docs_dir']
        # Directory where the site will be built
        site_dir = config['site_dir']
        # Suffix for output files
        suffix = self.config['output_suffix']

        for root, _, files in os.walk(docs_dir):
            for file in files:
                if file.endswith('.md'):
                    md_file = os.path.join(root, file)
                    with open(md_file, 'r') as f:
                        content = f.read()
                        if content.startswith('---'):
                            end = content.find('---', 3)
                            if end != -1:
                                front_matter = yaml.safe_load(content[3:end])
                                if front_matter.get('marp') == True:
                                    links = []
                                    for output_type in self.config['output_types']:
                                        # Determine the output directory and file name
                                        relative_path = os.path.relpath(root, docs_dir)
                                        output_dir = os.path.join(site_dir, relative_path)
                                        os.makedirs(output_dir, exist_ok=True)
                                        output_file = os.path.join(output_dir, file.replace('.md', f'{suffix}.{output_type}'))
                                        
                                        # Run Marp to generate the output file
                                        subprocess.run(['marp', f'--{output_type}', '--output', output_file, md_file])
                                        
                                        # Create a relative link to the output file
                                        relative_output_file = os.path.relpath(output_file, start=site_dir)
                                        # Adjust the relative path to ensure it points correctly
                                        relative_output_file = os.path.join(relative_path, file.replace('.md', f'{suffix}.{output_type}'))
                                        links.append(f"[{output_type.upper()} Slides]({relative_output_file})")
                                    
                                    # Remove existing links
                                    new_content = re.sub(r'\n*\[HTML Slides\]\(.*?\) \| \[PDF Slides\]\(.*?\)', '', content)
                                    
                                    # Append new links to the original markdown content
                                    new_content = new_content.rstrip() + "\n\n" + " | ".join(links) + "\n"
                                    
                                    # Only write if content has changed
                                    if new_content != content:
                                        with open(md_file, 'w') as f:
                                            f.write(new_content)
                                else:
                                    # Remove existing links if marp is not enabled
                                    new_content = re.sub(r'\n*\[HTML Slides\]\(.*?\) \| \[PDF Slides\]\(.*?\)', '', content)
                                    # Only write if content has changed
                                    if new_content != content:
                                        with open(md_file, 'w') as f:
                                            f.write(new_content)