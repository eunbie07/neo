// server.js
const express = require('express');
const fetch = require('node-fetch');
const cors = require('cors');
const app = express();
const port = 3000;

app.use(cors());
app.use(express.static('public'));

const KOSIS_URL = "https://kosis.kr/openapi/Param/statisticsParameterData.do";
const apiKey = "Yzg0MjIyMmVhMmNhODgyOGU0MjA2NDk1NGRkY2M3Yzg=";

app.get('/api/kosis', async (req, res) => {
  const fullUrl = `${KOSIS_URL}?method=getList&apiKey=${apiKey}&itmId=T001%2B&objL1=ALL&objL2=ALL&objL3=ALL&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=Y&newEstPrdCnt=3&orgId=154&tblId=DT_154013_24BB000901`;

  try {
    const response = await fetch(fullUrl);
    const data = await response.json();

    // 혹시 에러 메시지를 포함하고 있다면 확인
    if (data.length === 0 || data.error) {
      console.error("KOSIS 응답 이상:", data);
    }

    res.json(data);
  } catch (err) {
    console.error("KOSIS API 호출 실패:", err);
    res.status(500).json({ error: "데이터 요청 실패" });
  }
});

app.listen(port, () => {
  console.log(`✅ 서버 실행 중: http://localhost:${port}`);
});
