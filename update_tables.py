import re

with open('/Users/sean/Desktop/shop-4-main/database_demo.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix CSS
css_fix = """
        .table { margin-bottom: 0; font-size: 0.95rem; vertical-align: middle; white-space: nowrap; text-align: center; color: var(--text-main); }
        .table th { background-color: rgba(0,0,0,0.3) !important; color: var(--text-muted) !important; font-weight: 600; padding: 15px; border-bottom: 1px solid var(--border-color) !important; text-align: center; border-top: none; }
        .table td { padding: 15px; border-bottom: 1px solid var(--border-color) !important; color: var(--text-main) !important; background-color: transparent !important; }
        .table tbody tr { background-color: transparent !important; }
        .table tbody tr:hover { background-color: rgba(255,255,255,0.05) !important; }
"""

content = re.sub(r'\.table \{ margin-bottom: 0;.*?\.table tbody tr:hover \{ background-color: rgba\(255,255,255,0\.05\); \}', css_fix.strip(), content, flags=re.DOTALL)

# We need to insert the tables back.
tables_html = """
        <!-- 產品資料表 -->
        <div class="table-section">
            <div class="table-card">
                <div class="table-header">
                    <h4><i class="fa-solid fa-box-open text-info me-2"></i>產品資料表 (Product Table)</h4>
                    <span class="record-count">目前共有：37 筆</span>
                </div>
                <div class="table-responsive" style="max-height: 600px; overflow-y: auto;">
                    <table class="table align-middle">
                        <thead style="position: sticky; top: 0; z-index: 1;">
                            <tr><th>產品編碼</th><th>產品名稱</th><th>售價</th><th>產品描述</th><th>產品圖示</th><th>現有庫存</th><th>最後異動時間</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>2026055001</td><td>iPhone 15 Pro Max</td><td>NT$ 44900</td><td>鈦金屬設計，搭載 A17 Pro 晶片與超長電池續航力</td><td><img src="https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>120</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055002</td><td>Samsung Galaxy S24 Ultra</td><td>NT$ 43900</td><td>內建 Galaxy AI，體驗極致變焦與超強效能</td><td><img src="https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>115</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055003</td><td>iPad Pro M4</td><td>NT$ 34900</td><td>強效 M4 晶片，極致纖薄 OLED 顯示螢幕</td><td><img src="https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>108</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055004</td><td>Google Pixel 8 Pro</td><td>NT$ 33900</td><td>最先進的 AI 拍照，極佳的原生 Android 體驗</td><td><img src="https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>95</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055005</td><td>ASUS ROG Phone 8 Pro</td><td>NT$ 38990</td><td>頂級電競旗艦，帶來極致流暢的遊戲效能</td><td><img src="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>88</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055006</td><td>Xiaomi 14 Ultra</td><td>NT$ 34999</td><td>徠卡聯名影像大師，一吋大底光學變焦鏡頭</td><td><img src="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>76</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055007</td><td>Sony Xperia 1 VI</td><td>NT$ 39990</td><td>專業相機與發燒音質，極致的影音娛樂享受</td><td><img src="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>150</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055008</td><td>iPad Air 6</td><td>NT$ 19900</td><td>全新 M2 晶片，強悍效能與輕薄機身完美兼備</td><td><img src="https://images.unsplash.com/photo-1589739900243-4b52cd9b104e?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>102</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055009</td><td>Samsung Galaxy Tab S9</td><td>NT$ 23990</td><td>超大防潑水螢幕，為效率生產力而生</td><td><img src="https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>65</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055010</td><td>iPhone 15</td><td>NT$ 29900</td><td>動態島全新登場，強大相機與亮麗配色</td><td><img src="https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>92</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055011</td><td>Google Pixel 8a</td><td>NT$ 16490</td><td>精巧強大的智慧手機，提供完整 AI 工具與功能</td><td><img src="https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>80</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055012</td><td>Xiaomi Redmi Note 13 Pro</td><td>NT$ 9999</td><td>超高 CP 值旗艦體驗，2億畫素超清鏡頭</td><td><img src="https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>50</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055013</td><td>ASUS Zenfone 11 Ultra</td><td>NT$ 29990</td><td>大螢幕旗艦首選，AI 功能輕鬆應對生活</td><td><img src="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>70</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055027</td><td>OPPO Reno11 Pro</td><td>NT$ 16990</td><td>黃金焦段人像鏡頭，絕美輕薄外觀設計</td><td><img src="https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>110</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055015</td><td>Sony Xperia 10 VI</td><td>NT$ 13990</td><td>輕量手感搭配超強續航，日系美型防水手機</td><td><img src="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>85</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055031</td><td>Samsung Galaxy Fold 5</td><td>NT$ 56888</td><td>折疊大螢幕，商務多工處理極致流暢</td><td><img src="https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>96</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055017</td><td>iPhone 15 Plus</td><td>NT$ 32900</td><td>大螢幕大電量，動態島功能好用又吸睛</td><td><img src="https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>77</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055018</td><td>iPad 10th Gen</td><td>NT$ 11900</td><td>繽紛色彩，全螢幕設計，日常生活好幫手</td><td><img src="https://images.unsplash.com/photo-1589739900243-4b52cd9b104e?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>105</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055101</td><td>Logitech MX Master 3S</td><td>NT$ 3290</td><td>人體工學滑鼠，極致精準與舒適操作</td><td><img src="https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>126</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055102</td><td>Keychron K2 機械鍵盤</td><td>NT$ 2580</td><td>無線機械鍵盤，精巧緊湊的打字神器</td><td><img src="https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>110</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055103</td><td>MacBook Pro M3</td><td>NT$ 54900</td><td>蘋果強大 M3 晶片，專業工作者的頂級筆電</td><td><img src="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>95</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055104</td><td>ASUS RT-AX88U Pro 路由器</td><td>NT$ 8888</td><td>電競路由器，高速流暢且穩定的網路體驗</td><td><img src="https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>80</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055105</td><td>WD Black SN850X 2TB SSD</td><td>NT$ 5290</td><td>極速 PCIe Gen4 SSD，電競讀取瞬間載入</td><td><img src="https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>60</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055106</td><td>ROG Swift PG32UCDM 螢幕</td><td>NT$ 42900</td><td>32吋 4K OLED 頂級電競螢幕，極致色彩</td><td><img src="https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>45</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055107</td><td>Sony WH-1000XM5 耳機</td><td>NT$ 9900</td><td>業界領先的主動降噪耳罩式耳機，極致聽感</td><td><img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>85</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055201</td><td>Apple Watch Series 9</td><td>NT$ 13500</td><td>健康生活必備，手勢操作與先進感測器</td><td><img src="https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>72</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055202</td><td>Garmin Venu 3</td><td>NT$ 14990</td><td>專業運動與睡眠分析，全面掌握身體能量</td><td><img src="https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>68</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055203</td><td>AirPods Pro 2</td><td>NT$ 7490</td><td>主動降噪再升級，通透模式與適應性音訊</td><td><img src="https://images.unsplash.com/photo-1588449668365-d15e397f6787?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>110</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055204</td><td>Google Nest Hub 2</td><td>NT$ 3180</td><td>智慧螢幕管家，隨心控制全屋智能家電</td><td><img src="https://images.unsplash.com/photo-1543512214-318c7553f230?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>48</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055205</td><td>Dyson Purifier Cool</td><td>NT$ 18900</td><td>空氣清淨風扇，為全家人帶來純淨氣流</td><td><img src="https://images.unsplash.com/photo-1585338107529-13afc5f02586?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>62</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055206</td><td>Philips Hue 智慧燈泡</td><td>NT$ 4990</td><td>百萬種色彩氛圍燈光，智慧控制隨心調配</td><td><img src="https://images.unsplash.com/photo-1550985616-10810253b84d?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>55</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055207</td><td>Nintendo Switch OLED</td><td>NT$ 10480</td><td>全新 OLED 螢幕，隨時隨地享受精彩遊戲</td><td><img src="https://images.unsplash.com/photo-1578301978693-85fa9c0320b9?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>35</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055208</td><td>DJI Mini 4 Pro 空拍機</td><td>NT$ 22090</td><td>迷你航拍大師，全向避障與無損直拍</td><td><img src="https://images.unsplash.com/photo-1527977966376-1c8408f9f108?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>40</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055209</td><td>GoPro HERO12 Black</td><td>NT$ 14900</td><td>極致防手震運動相機，記錄每一刻熱血瞬間</td><td><img src="https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>50</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055210</td><td>HomePod 智慧音箱</td><td>NT$ 9300</td><td>沈浸式高品質音效，內建 Siri 語音助手</td><td><img src="https://images.unsplash.com/photo-1543512214-318c7553f230?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>90</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055211</td><td>Xiaomi 智慧攝影機 C400</td><td>NT$ 1095</td><td>超清 2.5K 畫質，360度全景智能看護</td><td><img src="https://images.unsplash.com/photo-1558002038-1055907df827?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>120</td><td>2026-04-16 22:00:01</td></tr>
                            <tr><td>2026055212</td><td>Dyson V15 Detect</td><td>NT$ 24900</td><td>雷射偵測吸塵器，智慧調整吸力，深度清潔</td><td><img src="https://images.unsplash.com/photo-1558317374-067fb5f30001?w=500&auto=format&fit=crop&q=60" class="product-img"></td><td>60</td><td>2026-04-16 22:00:01</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- 金流資料 -->
        <div class="table-section">
            <div class="table-card">
                <div class="table-header">
                    <h4><i class="fa-solid fa-credit-card text-warning me-2"></i>金流資料 (Payment Table)</h4>
                </div>
                <div class="table-responsive">
                    <table class="table align-middle">
                        <thead><tr><th>金流交易編號</th><th>對應訂單編號</th><th>付款方式</th><th>付款金額</th><th>付款狀態</th></tr></thead>
                        <tbody id="db-payment-body">
                            <tr><td colspan="5" class="empty-row">尚無金流資料。</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- 物流資料 -->
        <div class="table-section">
            <div class="table-card">
                <div class="table-header">
                    <h4><i class="fa-solid fa-truck-fast text-primary me-2"></i>物流資料 (Shipping Table)</h4>
                </div>
                <div class="table-responsive">
                    <table class="table align-middle">
                        <thead><tr><th>物流追蹤單號</th><th>對應訂單編號</th><th>配送方式</th><th>收件人</th><th>配送狀態</th></tr></thead>
                        <tbody id="db-shipping-body">
                            <tr><td colspan="5" class="empty-row">尚無物流資料。</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
"""

# Find where to insert tables_html
# We can insert it after the Member Table
parts = content.split('<!-- 隱藏的產品清單，用於初始化庫存基底 -->')
if len(parts) == 2:
    content = parts[0] + tables_html + '\n        <!-- 隱藏的產品清單，用於初始化庫存基底 -->' + parts[1]

# Now, we need to update the Javascript to populate db-payment-body and db-shipping-body based on orders
js_update = """
                // 金流與物流
                const payId = `PAY-${order.timestamp.toString().substring(7)}`;
                const shipId = `SHP-${order.timestamp.toString().substring(5)}`;
                
                paymentHtml += `<tr>
                    <td>${payId}</td>
                    <td>${orderId}</td>
                    <td>線上刷卡</td>
                    <td>NT$ ${order.total}</td>
                    <td><span class="status-badge status-success">已付款</span></td>
                </tr>`;

                const shipBadge = isCompleted 
                    ? '<span class="status-badge status-success">已配達</span>' 
                    : '<span class="status-badge status-pending">準備中</span>';
                    
                shippingHtml += `<tr>
                    <td>${shipId}</td>
                    <td>${orderId}</td>
                    <td>得正 3C 專屬物流</td>
                    <td>${order.customer}</td>
                    <td>${shipBadge}</td>
                </tr>`;
"""

# Let's insert the JS logic
# We need to find `let orderHtml = '';`
content = content.replace("let orderHtml = '';", "let orderHtml = '';\n            let paymentHtml = '';\n            let shippingHtml = '';")

# Replace `orderHtml += `<tr>` with the JS update
content = content.replace("orderHtml += `<tr>", js_update + "\n                orderHtml += `<tr>")

content = content.replace("document.getElementById('db-orders-body').innerHTML = orderHtml;", "document.getElementById('db-orders-body').innerHTML = orderHtml;\n                document.getElementById('db-payment-body').innerHTML = paymentHtml;\n                document.getElementById('db-shipping-body').innerHTML = shippingHtml;")

content = content.replace("document.getElementById('db-orders-body').innerHTML = '<tr><td colspan=\"6\" class=\"empty-row\">尚無訂單資料</td></tr>';", "document.getElementById('db-orders-body').innerHTML = '<tr><td colspan=\"6\" class=\"empty-row\">尚無訂單資料</td></tr>';\n                document.getElementById('db-payment-body').innerHTML = '<tr><td colspan=\"5\" class=\"empty-row\">尚無金流資料。</td></tr>';\n                document.getElementById('db-shipping-body').innerHTML = '<tr><td colspan=\"5\" class=\"empty-row\">尚無物流資料。</td></tr>';")

with open('/Users/sean/Desktop/shop-4-main/database_demo.html', 'w', encoding='utf-8') as f:
    f.write(content)
