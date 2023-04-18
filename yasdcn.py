from sys import exit
from IPython.display import HTML


def print_html(content='', color='#FFFFFF'):
    display(HTML(f'<p style="font-size: 18px; font-weight: bold; color: {color};">{content}</p>'))


def download(url, output_path='/content'):
    url = url.replace(' ', '%20')

    if 'civitai.com' in url:
        if not '/api/download/models/' in url:
            exit(print_html('❌ Please copy the url from the download button on the top right corner', '#F44336'))

        !wget -nc -P '{output_path}' --content-disposition -q --show-progress --progress=bar:force 2>&1 '{url}'
    elif 'huggingface.co' in url:
        if '/blob/' in url:
            url = url.replace('/blob/', '/resolve/')

        !wget -nc -P '{output_path}' -q --show-progress --progress=bar:force 2>&1 '{url}'
    elif 'drive.google.com' in url:
        !gdown '{url}' -O '{output_path}/'
    else:
        !wget -nc -P '{output_path}' -q --show-progress --progress=bar:force 2>&1 '{url}'


main_dir = f'/content/stable-diffusion'
webui_dir = f'{main_dir}/stable-diffusion-webui'
model_dir = f'{webui_dir}/models/Stable-diffusion'
vae_dir = f'{webui_dir}/models/VAE'
lora_dir = f'{webui_dir}/models/Lora'
hypernetwork_dir = f'{webui_dir}/models/hypernetworks'
upscaler_dir = f'{webui_dir}/models/ESRGAN'
embedding_dir = f'{webui_dir}/embeddings'
extension_dir = f'{webui_dir}/extensions'
