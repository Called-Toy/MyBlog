def user_context_processor(request):

    adminuser = request.session.get('adminuser')

    # 确保 adminuser 是一个字典
    if isinstance(adminuser, dict):
        return {'loginuser': adminuser['username'],'avatar':adminuser['avatar']}
    else:
        # 如果 adminuser 不是字典，返回空字典或进行其他处理
        return {}
