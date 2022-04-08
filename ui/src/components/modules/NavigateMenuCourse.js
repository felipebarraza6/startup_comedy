import React, { useContext, useState, useEffect } from 'react'
import { Menu } from 'antd'
import { AudioOutlined, CheckCircleOutlined } from '@ant-design/icons'
import api from '../../api/endpoints'

const NavigateMenuCourse = ({ modules, setState, state, course }) => {

  const [views, setView] = useState(null)
  
  const getViews = async()=> {
        const rq = await api.viewsVideo.list_view_video({course: course}).then((x)=> {
          setView(x.results)
          console.log(x.results)
        })

      }

  useEffect(()=> {  
      getViews()
  }, [])


  return(<Menu mode='inline' defaultOpenKeys={['1', '2', '3', '4', '5', '6']}>
        <Menu.Item onClick={()=>setState({...state, video:null, resources:null})}>INTRODUCCIÓN</Menu.Item>
        {modules.map((x)=> <Menu.SubMenu icon={<AudioOutlined />} title={x.title} key={x.id}>
            {x.videos.map((z)=>
              <Menu.Item key={z.id} 
                icon={views && <>{views.filter(e=>e.video.id === z.id).length>0 && <CheckCircleOutlined style={styles.icon} />}</>}
                onClick={async()=> {
                  if(!views.filter(e=>e.video.id === z.id).length>0){
                    console.log("asd")
                    const request = await api.viewsVideo.create_view_video({
                      course: course,
                      video: z.id
                    }).then((x)=>{
                      getViews()
                    })
                  }
                  setState({
                    ...state,
                    video: { 
                      title: z.title,
                      url: z.url 
                    },
                    resources: z.resources
                  })}}>
               
                {z.title}
              </Menu.Item>)}
          </Menu.SubMenu>)}
    </Menu>)

}

const styles = {
  icon: {
    fontSize:'20px',
    color: 'green'
  }
}


export default NavigateMenuCourse