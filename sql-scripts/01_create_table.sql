-- 创建数据库
-- 创建用户表
create table IF NOT EXISTS user_info (
-- uid, 整数 无符号数 自增 主键
uid int unsigned auto_increment primary key,
-- username 不可为null, 不可重复
username char(255) not null unique,
password char(255) not null,
-- create_time 时间类型 默认为当前时间
create_time datetime DEFAULT CURRENT_TIMESTAMP,
-- update_time 时间类型 默认为当前时间 update时更新为最新时间
update_time datetime DEFAULT CURRENT_TIMESTAMP on update current_timestamp
);
-- 创建token表
create table IF NOT EXISTS user_token (
    tid int unsigned auto_increment primary key,
    uid int unsigned,
    token char(255) not null unique,
    expire_time datetime not null,
    create_time datetime DEFAULT CURRENT_TIMESTAMP,
    update_time datetime DEFAULT CURRENT_TIMESTAMP on update
current_timestamp,
-- uid 外键 关联user_info.uid
    foreign key (uid) references user_info(uid)
);