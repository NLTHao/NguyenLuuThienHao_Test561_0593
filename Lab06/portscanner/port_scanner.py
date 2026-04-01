import socket

# Danh sách các cổng phổ biến để quét
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]

def scan_common_ports(target_domain, timeout=1):
    open_ports = []
    try:
        # Phân giải tên miền sang địa chỉ IP
        target_ip = socket.gethostbyname(target_domain)
        print(f"\n--- Đang quét mục tiêu: {target_domain} ({target_ip}) ---")
        print("Vui lòng đợi trong giây lát...\n")
    except socket.gaierror:
        print("Lỗi: Không thể phân giải tên miền. Kiểm tra lại kết nối mạng.")
        return []

    for port in COMMON_PORTS:
        # Tạo một đối tượng socket (AF_INET là IPv4, SOCK_STREAM là TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Thiết lập thời gian chờ (timeout) để không đợi quá lâu ở cổng đóng
        s.settimeout(timeout)
        
        # Thực hiện kết nối thử (connect_ex trả về 0 nếu thành công)
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[+] Port {port}: OPEN")
            open_ports.append(port)
        
        # Đóng socket sau mỗi lần thử
        s.close()
            
    return open_ports

def main():
    target_domain = input("Enter the target domain (vd: hutech.edu.vn): ").strip()
    if not target_domain:
        return

    open_ports = scan_common_ports(target_domain)

    print("-" * 40)
    if open_ports:
        print(f"KẾT QUẢ: Tìm thấy {len(open_ports)} cổng đang mở.")
        print(f"Danh sách cổng: {open_ports}")
    else:
        print("KẾT QUẢ: Không tìm thấy cổng nào mở hoặc server đã chặn quét.")
    print("-" * 40)

if __name__ == '__main__':
    main()