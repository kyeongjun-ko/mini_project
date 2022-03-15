def popup_html(row, df):
    i = row
    text1 = df['store_name'].iloc[i]
    text2 = df['open_days'].iloc[i]
    text3 = df['open_hours'].iloc[i]
    text4 = df['ppl'].iloc[i]
    text5 = df['addr'].iloc[i]
    text6 = df['extra_info'].iloc[i]
    text7 = df['siteurl'].iloc[i]

    html = """<!DOCTYPE html>
    <html>
    <head>

    </head>
    <body>
    <pre>
<strong>{}""".format(text1) + """</strong><br>
영업시간: {} {} """.format(text2, text3) + """<br>
제공대상: {}""".format(text4) + """<br>
주소: {}""".format(text5) + """<br>
비고: {}""".format(text6) + """

홈페이지: <a href={}""".format(text7) + """>{}""".format(text7) + """</a>
</pre>
    </body>
    """

    return html