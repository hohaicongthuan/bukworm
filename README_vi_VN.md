# bukworm

> Read the English version of this `README.md` file [here](README.md)

Phần mềm đọc sách điện tử cho phép tùy chỉnh giao diện.

***LƯU Ý: PHẦM MỀM NÀY ĐANG ĐƯỢC PHÁT TRIỂN VÀ CHƯA SẴN SÀNG ĐỂ SỬ DỤNG.***

## Các tính năng trong tương lai
- Hỗ trợ xem định dạng PDF
- Hỗ trợ xem các định dạng tài liệu của Microsoft Office (DOCX, PPTX, XLSX)
- Hỗ trợ xem định dạng Markdown
- Hỗ trợ xem các định dạng ảnh phổ biến (JPG, PNG, QOI, v.v.)
- Cho phép người dùng có thể tùy chỉnh kiểu font, cỡ font, màu font, màu trang, màu nền, v.v.

## Ảnh chụp màn hình giao diện

TODO

## Yêu cầu trước khi dùng phần mềm

Yêu cầu máy tính cài sẵn `Python 3.7` hoặc mới hơn, `PIP` và `virtualenv` để dùng bukworm

### Ở các hệ điều hành nhân Linux

`virtualenv` có thể cài bằng lệnh:

```
pip3 install virtualenv
```

### Bên Windows

Bên Windows thì cần cài thêm _Microsoft Edge WebView 2 Runtime_. Nếu bạn dùng Windows 10, thì khả năng cao là nó đã được cài sẵn rồi. Nếu bạn dùng Windows 7, tải file cài ở [đây](https://developer.microsoft.com/en-us/microsoft-edge/webview2/#download-section) (nên chọn _Evergreen Standalone Installer_). Kiểm tra xem _Microsoft Edge WebView 2 Runtime_ đã được cài chưa bằng cách mở `Control Panel > Programs and Features` và tìm trong danh sách.

`virtualenv` có thể được cài bằng lệnh:

```
pip install virtualenv
```

## Làm thế nào để chạy?

Hãy chắc chắn rằng bạn đã cài tất cả những phần mềm yêu cầu ở mục **"Yêu cầu trước khi dùng phần mềm"** trước khi tiếp tục.

Chỉ cần chạy file `run.py`.

> _Lưu ý là lần đầu tiên script chạy thì nó sẽ kiểm tra xem có môi trường ảo nào tạo ra chưa, nếu chưa thì nó sẽ tạo một môi trường ảo và tự cài các phần mềm yêu cầu trong file `requirements.txt` nên lần đầu chạy hãy chắc chắn rằng bạn có sẵn **kết nối internet**_

### Bên Linux (và có lẽ là bên MacOS luôn??*)

Mở app terminal và chạy:

```
python3 run.py
```

HOẶC cấp quyền thực thi cho script (bạn chỉ cần cấp quyền đúng MỘT LẦN duy nhất) bằng lệnh:

```
chmod +x run.py
```

VÀ sau đó dùng:

```
./run.py
```

để chạy

### Bên Windows

Mở Command-line và chạy:

```
python run.py
```


## Làm thế nào để build?

Hãy chắc chắn rằng bạn đã cài tất cả những phần mềm yêu cầu ở mục **"Yêu cầu trước khi dùng phần mềm"** trước khi tiếp tục.

> _Lưu ý là lần đầu tiên script chạy thì nó sẽ kiểm tra xem có môi trường ảo nào tạo ra chưa, nếu chưa thì nó sẽ tạo một môi trường ảo và tự cài các phần mềm yêu cầu trong file `requirements.txt` nên lần đầu chạy hãy chắc chắn rằng bạn có sẵn **kết nối internet**_

> _Lưu ý: hiện tại Bukworm dùng `pyinstaller` để build ra file nhị phân nhưng file build bằng `pyinstaller` thường khá lớn (100+ MB). Mình đang thử các công cụ build khác nhau để giảm kích thước file xuống nên phần build trong tương lai chắc chắn sẽ thay đổi._

Sau đó chạy file `build.py`. Kết quả build sẽ được lưu ở thư mục `dist`.

### Bên Linux (và có lẽ là bên MacOS luôn??*)

Mở app terminal và chạy:

```
python3 build.py
```

HOẶC cấp quyền thực thi cho script (bạn chỉ cần cấp quyền đúng MỘT LẦN duy nhất) bằng lệnh:

```
chmod +x build.py
```

VÀ sau đó dùng:

```
./build.py
```

để build

### Bên Windows

Mở Command-line và chạy:

```
python build.py
```

## Giấy phép
_Đang xem xét..._

> \* Mình chưa bao giờ dùng MacOS nên không biết là phần mềm này có chạy được trên đấy không, nhưng mà mình nghĩ chắc là được vì Python hỗ trợ nhiều nền tảng mà (cross-platform).
