import traceback
import sys

"""
Se adicionarmos a função traceback.print_stack(file=sys.stdout) conseguimos
ver quais os itens presentes na call stack do Python. Para que vocês possam
visualizar basta copiar o código abaixo e executá-lo no modo iterativo do
interpretador:
"""


def load_video(video_path):
    print('Carregando vídeo do caminho:', video_path)
    traceback.print_stack(file=sys.stdout)
    return 'fake vídeo'


def process_video(video_path):
    print('Carregando vídeo...')
    loaded_video = load_video(video_path)
    return loaded_video


process_video('path/to/my/video')