import React, { useContext }  from 'react' 

import { Menu, Tag, Layout } from 'antd'
import { LogoutOutlined, UserOutlined } from '@ant-design/icons'
import { Link } from 'react-router-dom' 
//Auth Context
import { AuthContext } from '../../App'
const { Header } = Layout

const MenuHeader = () => {   

    const { dispatch, state } = useContext(AuthContext)


    const Logout = () => dispatch({
            type: 'LOGOUT'
    })

    return (<>   
            <Menu mode="horizontal" theme="dark" style={styles.rightMenu}>
                <Menu.Item style={styles.menuNoHovereable}>
                  <Link to='profile'>
                  <UserOutlined  />
                  @{state.user.username}
                  </Link>
                </Menu.Item>
                <Menu.Item style = {styles.menuNoHovereable}  >
                  <Tag color='geekblue' >{state.user.first_name}</Tag>
                  <Tag color='geekblue' >{state.user.last_name}</Tag>
                </Menu.Item>
                <Menu.Item onClick={Logout}>
                    <LogoutOutlined />
                    Cerrar Sesión
                </Menu.Item>
            </Menu>                
    </>)

}


const styles = {
  menuNoHovereable: {
    backgroundColor: '#001529',
  },
  rightMenu: {
    position: 'absolute',
    top: 0,
    right: 0
  }
}

export default MenuHeader
