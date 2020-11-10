box.cfg{
    listen=3301
}

box.schema.user.grant('guest', 'read', 'universe', nil, {if_not_exists=true})


box.once("blanket", function()
    box.schema.sequence.create('photo_S')
    box.schema.space.create('photo', {
        if_not_exists = true,
        format={
             {name = 'id', type = 'unsigned'},
             {name = 'photo', type = 'string'}
        }
    })
    box.space.photo:create_index('id', {
        sequence = 'photo_S',
        parts = {'id'}
    })  

    box.schema.sequence.create('message_S')
    box.schema.space.create('message', {
        if_not_exists = true,
        format={
             {name = 'id', type = 'unsigned'},
             {name = 'message', type = 'string'}
        }
    })
     box.space.message:create_index('id', {
        sequence = 'message_S',
        parts = {'id'}
    })

    box.schema.space.create('user', {
        if_not_exists = true,
        format={
            {name = 'user_id', type = 'string'},
            {name = 'update', type = 'boolean'},
            {name = 'data_mailing', type = 'string'},
            {name = 'is_mailing', type = 'boolean'},
            {name = 'send_message', type = 'array'},
            {name = 'count_photo', type = 'unsigned'},
            {name = 'line', type = 'unsigned'}
        }
    })
    box.space.user:create_index('user_id', {
        type = 'hash',
        parts = {'user_id'},
        if_not_exists = true,
        unique = true
    })      
end
)
