from path import Path
from matplotlib import pyplot as plt
import librosa
import librosa.display
import numpy as np
# GTZAN 数据库下载的文件位置
data_dir = 'D:\\迅雷下载\\genres\\'
genres = ['blues', 'classical', 'country', 'disco', 
   'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
for genre in genres:
    d_in = Path(data_dir+genre)
    for f in d_in.files('*.au'):
        fig = plt.figure(figsize=(12, 4))
        y, sr = librosa.core.load(f)
        b = librosa.feature.melspectrogram(y=y, sr=sr)
        librosa.display.specshow(librosa.power_to_db(b, ref=np.max))
        plt.tight_layout()
        output_file_path = '.\\genres\\{}\\{}.png'.format(genre, f.name)
        d_out = Path('.\\genres\\'+genre)
        d_out.mkdir_p()
        print(output_file_path)
        plt.savefig(output_file_path)
        plt.close(fig)






