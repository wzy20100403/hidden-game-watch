/**
 * 关卡与道具数据（全部原创，不含任何商业游戏素材）。
 *
 * 每关是一个"点物件 → 触发状态 → 用道具/顺序破解"的小机关，
 * 连续被妈妈发现 3 次就重来。物件坐标是 390×296 房间画布内的像素。
 */
export const ITEMS = {
  torch: { id: 'torch', name: '手电筒', img: '/assets/images/flashlight.png' },
  ice: { id: 'ice', name: '冰块', img: '/assets/images/ice.png' },
  key: { id: 'key', name: '小钥匙', img: '/assets/images/key.png' },
  key2: { id: 'key2', name: '旧钥匙', img: '/assets/images/key2.png' },
  key3: { id: 'key3', name: '铜钥匙', img: '/assets/images/key3.png' },
  towel: { id: 'towel', name: '毛巾', img: '/assets/images/towel.png' },
  rag: { id: 'rag', name: '抹布', img: '/assets/images/rag.png' }
}

export const LEVELS = [
  {
    name: '卧室',
    hint: '先找光，再找能垫脚的东西。',
    objects: [
      { id: 'bed', name: '床', img: '/assets/images/bed.png', x: 4, y: 150, s: 120 },
      { id: 'wardrobe', name: '衣柜', img: '/assets/images/wardrobe.png', x: 262, y: 128, s: 110 },
      { id: 'desk', name: '书桌', img: '/assets/images/desk.png', x: 138, y: 158, s: 100 },
      { id: 'chair', name: '椅子', img: '/assets/images/chair.png', x: 244, y: 196, s: 62 },
      { id: 'rug', name: '地毯', img: '/assets/images/rug.png', x: 20, y: 244, s: 80 }
    ]
  },
  {
    name: '厨房',
    hint: '冰块降温，微波炉烘干。',
    objects: [
      { id: 'fridge', name: '冰箱', img: '/assets/images/fridge.png', x: 6, y: 110, s: 96 },
      { id: 'cabinet', name: '橱柜', img: '/assets/images/cabinet.png', x: 270, y: 104, s: 104 },
      { id: 'microwave', name: '微波炉', img: '/assets/images/microwave.png', x: 282, y: 42, s: 64 },
      { id: 'pot', name: '汤锅', img: '/assets/images/pot.png', x: 150, y: 112, s: 96 },
      { id: 'basket', name: '果篮', img: '/assets/images/basket.png', x: 250, y: 224, s: 64 },
      { id: 'trash', name: '垃圾桶', img: '/assets/images/trash.png', x: 30, y: 226, s: 56 }
    ]
  },
  {
    name: '浴室',
    hint: '先断电，再把游戏机擦干。',
    objects: [
      { id: 'washer', name: '洗衣机', img: '/assets/images/washer.png', x: 8, y: 150, s: 108 },
      { id: 'sink', name: '洗手台', img: '/assets/images/sink.png', x: 128, y: 196, s: 68 },
      { id: 'bathtub', name: '浴缸', img: '/assets/images/bathtub.png', x: 202, y: 180, s: 116 },
      { id: 'mirror', name: '镜子', img: '/assets/images/mirror.png', x: 36, y: 30, s: 64 },
      { id: 'towel', name: '毛巾', img: '/assets/images/towel.png', x: 146, y: 26, s: 64 },
      { id: 'outlet', name: '插座', img: '/assets/images/outlet.png', x: 330, y: 144, s: 44 }
    ]
  },
  {
    name: '阳台',
    hint: '钥匙和抹布，缺一不可。',
    objects: [
      { id: 'shoerack', name: '鞋柜', img: '/assets/images/shoerack.png', x: 4, y: 160, s: 80 },
      { id: 'toolbox', name: '工具箱', img: '/assets/images/toolbox.png', x: 36, y: 200, s: 92 },
      { id: 'wateringcan', name: '浇水壶', img: '/assets/images/wateringcan.png', x: 146, y: 214, s: 64 },
      { id: 'flowerpot', name: '花盆', img: '/assets/images/flowerpot.png', x: 222, y: 206, s: 64 },
      { id: 'carton', name: '纸箱', img: '/assets/images/carton.png', x: 306, y: 212, s: 66 }
    ]
  },
  {
    name: '妈妈房间',
    hint: '先让妈妈分心，再开包上的锁。',
    objects: [
      { id: 'suitcase', name: '行李箱', img: '/assets/images/suitcase.png', x: 4, y: 190, s: 84 },
      { id: 'mom', name: '妈妈', img: '/assets/images/mom.png', x: 140, y: 120, s: 100 },
      { id: 'radio', name: '收音机', img: '/assets/images/radio.png', x: 296, y: 120, s: 62 },
      { id: 'vanity', name: '化妆台', img: '/assets/images/vanity.png', x: 250, y: 180, s: 100 },
      { id: 'handbag', name: '手提包', img: '/assets/images/handbag.png', x: 36, y: 212, s: 78 },
      { id: 'pillow', name: '枕头', img: '/assets/images/pillow.png', x: 140, y: 226, s: 72 }
    ]
  }
]

// 每天允许的疑心上限：从宽松到紧张
export const DIFFICULTY = [8, 6, 5, 3, 3]

export const ENDING = {
  title: '全部找到！',
  msg: '妈妈叹了口气：「只准玩十分钟哦。」',
  sub: '五关全通关 · 你赢了妈妈',
  btn: '再玩一次'
}


// 每天妈妈把游戏机藏在不同的房间；左右箭头可随时换房间。
export const DAYS = [
  { room: 0, hint: '掀开被子找手电，照亮衣柜顶。' },
  { room: 1, hint: '冰块在冰箱，毛巾在浴室。' },
  { room: 2, hint: '洗衣机的钥匙在阳台浇水壶下。' },
  { room: 3, hint: '抹布在厨房的橱柜里。' },
  { room: 4, hint: '卧室地毯下有一把钥匙，妈妈怕收音机。' }
]
