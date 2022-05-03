import React, { useState } from 'react'
import { Modal, Button, Input, Spin, List, Typography} from 'antd'
import WooCommerceRestApi from "@woocommerce/woocommerce-rest-api"
import apil from '../../api/endpoints'



const ModalNewCourse = () => {
  const [visible, setVisible] = useState(false)
  const [data, setData]= useState({})
  const [loading, setLoading] = useState(false) 
  const [listCodes, setCodes] = useState([])
  
  const user = JSON.parse(localStorage.getItem('user') || null)


  const api = new WooCommerceRestApi({
    url: "https://startupcomedy.org/",
    consumerKey: "ck_b7b28ce429747c3854b81322682de59682dfeb21",
    consumerSecret: "cs_f9dc85f346cc45771ca63173840810bafb855e4e",
    version: "wc/v3"
  })


  return(<><Modal visible={visible} onCancel={()=>setVisible(false)} title='AGREGAR CURSO COMPRADO' okText='AGREGAR'
              onOk={async()=> {
                data.items.map(async(x)=>{
                    const rq = await apil.courses.get_retrieve_course(x.product_id).then((rq)=> {
                      const rq2 = apil.courses.update_course(x.product_id, {"authorized_user": [
                        ...rq.authorized_user,
                        user.id
                      ]}).then((r)=>Modal.success({title:'CURSO AGREGADO!'}))
                    })
                    console.log(user.id)
                }) 
              } }
            >

              <h4>CODIGO DE PEDIDO #{data.code}</h4>
              <Input onChange={(e)=>setData({...data, code:e.target.value })} />
            <Button onClick={async()=> {
              setLoading(true)
              const rq = await api.get(`orders/${data.code}`)
                  .then((response) => {
                  console.log(response.data);
                  setLoading(false)
                  setData({
                    ...data,
                    items: response.data.line_items
                  })
                  }).catch((error) => {
                    Modal.error({title:'NO SE ENCONTRO NINGUN PEDIDO CON EL CODIGO'})
                    setData({...data, items:[]})
                    setLoading(false)
                  })
            }
            } type='primary' style={{marginTop:'10px', marginBottom:'10px'}} size='small'>VALIDAR CODIGO</Button>
            {loading && <Spin  style={{marginLeft:'20px'}}/>}
            {data.items && <>
              <List
                header={<div>Cursos comprados</div>}
                bordered
                dataSource={data.items}
                renderItem={item => (
                  <List.Item>
                    <Typography.Text mark>[{item.product_id}]</Typography.Text> {item.name}
                  </List.Item>
                )}
              />
              </>}
            </Modal>
            <Button onClick={()=> setVisible(true)}>(+) AGREGAR CURSO COMPRADO</Button>
        </>)

}


export default ModalNewCourse
