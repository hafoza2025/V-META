from pywebio import start_server
from pywebio.input import input
from pywebio.output import put_html, toast
import pytube
import os

def download_video(url):
    if 'youtube.com' not in url and 'youtu.be' not in url:
        toast("يرجى إدخال رابط فيديو صالح من يوتيوب")
        return

    try:
        video = pytube.YouTube(url)
        stream = video.streams.get_highest_resolution()
        download_path = os.path.expanduser('~/Downloads')  # تحديد المسار تلقائيًا
        stream.download(download_path)
        toast(f'تم تحميل الفيديو بنجاح إلى: {download_path}')
    except pytube.exceptions.PytubeError as e:
        toast(f"حدث خطأ أثناء تحميل الفيديو: {str(e)}")
    except Exception as e:
        toast(f"حدث خطأ غير متوقع: {str(e)}")

def App():
    put_html('<img src="https://cdn0.iconfinder.com/data/icons/social-media-with-fill/64/youtube_colour-512.png" width="100">')
    put_html('<h3>برنامج تحميل الفيديوهات</h3>').style('text-align:right;')
    put_html('<p>تطبيق تحميل الفيديو من اليوتيوب بلغة بايثون</p>').style('text-align:right;')

    url = input('أدخل رابط الفيديو من يوتيوب:', placeholder='الصق رابط الفيديو هنا')

    download_video(url)

    put_html('<hr><br>')
    put_html('<h2>تم الانتهاء من تحميل الفيديو</h2>').style('text-align:center;')
    put_html('<hr><br>')

# بدء الخادم على البورت 2035
start_server(App, port=8080, debug=True)
