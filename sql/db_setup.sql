use test;
CREATE TABLE `t_user` (
  `Fid` int(11) NOT NULL AUTO_INCREMENT,
  `Fuser` varchar(32) NOT NULL DEFAULT '',
  `Fmodify_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  PRIMARY KEY (`Fid`),
  UNIQUE KEY `uq_user` (`Fuser`),
  KEY `idx_modify_time` (`Fmodify_time`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;