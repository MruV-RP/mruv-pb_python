# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from punishments import punishments_pb2 as punishments_dot_punishments__pb2


class MruVPunishmentsServiceStub(object):
  """This service provides interface for managing punishments for players.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Punish = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/Punish',
        request_serializer=punishments_dot_punishments__pb2.PunishRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.PunishResponse.FromString,
        )
    self.Ban = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/Ban',
        request_serializer=punishments_dot_punishments__pb2.BanRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.BanResponse.FromString,
        )
    self.Block = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/Block',
        request_serializer=punishments_dot_punishments__pb2.BlockRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.BlockResponse.FromString,
        )
    self.Warn = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/Warn',
        request_serializer=punishments_dot_punishments__pb2.WarnRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.WarnResponse.FromString,
        )
    self.AdminJail = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/AdminJail',
        request_serializer=punishments_dot_punishments__pb2.AdminJailRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.AdminJailResponse.FromString,
        )
    self.MuteGlobalChats = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/MuteGlobalChats',
        request_serializer=punishments_dot_punishments__pb2.MuteGlobalChatsRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.MuteGlobalChatsResponse.FromString,
        )
    self.UnBan = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/UnBan',
        request_serializer=punishments_dot_punishments__pb2.UnBanRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.UnBanResponse.FromString,
        )
    self.UnBlock = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/UnBlock',
        request_serializer=punishments_dot_punishments__pb2.UnBlockRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.UnBlockResponse.FromString,
        )
    self.UnWarn = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/UnWarn',
        request_serializer=punishments_dot_punishments__pb2.UnWarnRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.UnWarnResponse.FromString,
        )
    self.UnAdminJail = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/UnAdminJail',
        request_serializer=punishments_dot_punishments__pb2.UnAdminJailRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.UnAdminJailResponse.FromString,
        )
    self.UnMuteGlobalChats = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/UnMuteGlobalChats',
        request_serializer=punishments_dot_punishments__pb2.UnMuteGlobalChatsRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.UnMuteGlobalChatsResponse.FromString,
        )
    self.GetPlayerBans = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/GetPlayerBans',
        request_serializer=punishments_dot_punishments__pb2.GetPlayerBansRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.GetPlayerBansResponse.FromString,
        )
    self.GetPlayerWarns = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/GetPlayerWarns',
        request_serializer=punishments_dot_punishments__pb2.GetPlayerWarnsRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.GetPlayerWarnsResponse.FromString,
        )
    self.GetPlayerAdminJail = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/GetPlayerAdminJail',
        request_serializer=punishments_dot_punishments__pb2.GetPlayerAdminJailRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.GetPlayerAdminJailResponse.FromString,
        )
    self.GetBan = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/GetBan',
        request_serializer=punishments_dot_punishments__pb2.GetBanRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.BanMessage.FromString,
        )
    self.GetWarn = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/GetWarn',
        request_serializer=punishments_dot_punishments__pb2.GetWarnRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.WarnMessage.FromString,
        )
    self.GetBlock = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/GetBlock',
        request_serializer=punishments_dot_punishments__pb2.GetBlockRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.BlockMessage.FromString,
        )
    self.IsPlayerBanned = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/IsPlayerBanned',
        request_serializer=punishments_dot_punishments__pb2.IsPlayerBannedRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.IsPlayerBannedResponse.FromString,
        )
    self.IsCharacterBlocked = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/IsCharacterBlocked',
        request_serializer=punishments_dot_punishments__pb2.IsCharacterBlockedRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.IsCharacterBlockedResponse.FromString,
        )
    self.IsCharacterJailed = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/IsCharacterJailed',
        request_serializer=punishments_dot_punishments__pb2.IsCharacterJailedRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.IsCharacterJailedResponse.FromString,
        )
    self.WatchBans = channel.unary_stream(
        '/mruv.punishments.MruVPunishmentsService/WatchBans',
        request_serializer=punishments_dot_punishments__pb2.WatchBansRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.BanMessage.FromString,
        )
    self.WatchBlocks = channel.unary_stream(
        '/mruv.punishments.MruVPunishmentsService/WatchBlocks',
        request_serializer=punishments_dot_punishments__pb2.WatchBlocksRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.BlockMessage.FromString,
        )
    self.WatchWarns = channel.unary_stream(
        '/mruv.punishments.MruVPunishmentsService/WatchWarns',
        request_serializer=punishments_dot_punishments__pb2.WatchWarnsRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.WarnMessage.FromString,
        )
    self.WatchAdminJails = channel.unary_stream(
        '/mruv.punishments.MruVPunishmentsService/WatchAdminJails',
        request_serializer=punishments_dot_punishments__pb2.WatchAdminJailsRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.AdminJailMessage.FromString,
        )
    self.WatchUnBans = channel.unary_stream(
        '/mruv.punishments.MruVPunishmentsService/WatchUnBans',
        request_serializer=punishments_dot_punishments__pb2.WatchUnBansRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.UnBanMessage.FromString,
        )
    self.WatchUnBlocks = channel.unary_stream(
        '/mruv.punishments.MruVPunishmentsService/WatchUnBlocks',
        request_serializer=punishments_dot_punishments__pb2.WatchUnBlocksRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.UnBlockMessage.FromString,
        )
    self.WatchUnWarns = channel.unary_stream(
        '/mruv.punishments.MruVPunishmentsService/WatchUnWarns',
        request_serializer=punishments_dot_punishments__pb2.WatchUnWarnsRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.UnWarnMessage.FromString,
        )
    self.WatchUnAdminJails = channel.unary_stream(
        '/mruv.punishments.MruVPunishmentsService/WatchUnAdminJails',
        request_serializer=punishments_dot_punishments__pb2.WatchUnAdminJailsRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.UnAdminJailMessage.FromString,
        )
    self.WatchPlayerPunishments = channel.unary_stream(
        '/mruv.punishments.MruVPunishmentsService/WatchPlayerPunishments',
        request_serializer=punishments_dot_punishments__pb2.WatchPlayerPunishmentsRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.WatchPlayerPunishmentsResponse.FromString,
        )
    self.WatchPlayerAcquittals = channel.unary_stream(
        '/mruv.punishments.MruVPunishmentsService/WatchPlayerAcquittals',
        request_serializer=punishments_dot_punishments__pb2.WatchPlayerAcquittalsRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.WatchPlayerAcquittalsResponse.FromString,
        )
    self.WatchPunishments = channel.unary_stream(
        '/mruv.punishments.MruVPunishmentsService/WatchPunishments',
        request_serializer=punishments_dot_punishments__pb2.WatchPunishmentsRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.WatchPunishmentsResponse.FromString,
        )
    self.WatchAcquittals = channel.unary_unary(
        '/mruv.punishments.MruVPunishmentsService/WatchAcquittals',
        request_serializer=punishments_dot_punishments__pb2.WatchAcquittalsRequest.SerializeToString,
        response_deserializer=punishments_dot_punishments__pb2.WatchAcquittalsResponse.FromString,
        )


class MruVPunishmentsServiceServicer(object):
  """This service provides interface for managing punishments for players.
  """

  def Punish(self, request, context):
    """Punish player with choosen punishment type.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Ban(self, request, context):
    """Ban player on account and/or ip.
    If ban_time is 0, ban will never expire.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Block(self, request, context):
    """Block player character.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Warn(self, request, context):
    """Warn player.
    If warn_time is 0, warn will never expire.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AdminJail(self, request, context):
    """Put player in an admin jail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MuteGlobalChats(self, request, context):
    """Mute player global chats.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnBan(self, request, context):
    """Deactivate a specific player ban.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnBlock(self, request, context):
    """Deactivate a character block.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnWarn(self, request, context):
    """Deactivate a specific player warning. If a player was banned by reaching the warning limit, a player will be unbanned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnAdminJail(self, request, context):
    """Remove player from admin jail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnMuteGlobalChats(self, request, context):
    """
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPlayerBans(self, request, context):
    """Get all player bans.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPlayerWarns(self, request, context):
    """Get all player warns.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPlayerAdminJail(self, request, context):
    """Get player admin jail time.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBan(self, request, context):
    """Get ban info.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetWarn(self, request, context):
    """Get warn info.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlock(self, request, context):
    """Get block info.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def IsPlayerBanned(self, request, context):
    """Check is player or ip banned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def IsCharacterBlocked(self, request, context):
    """Check is character is blocked.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def IsCharacterJailed(self, request, context):
    """
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchBans(self, request, context):
    """Subscribe to ban events.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchBlocks(self, request, context):
    """Subscribe to block events.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchWarns(self, request, context):
    """Subscribe to warn events.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchAdminJails(self, request, context):
    """Subscribe to admin jail events.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchUnBans(self, request, context):
    """Subscribe to unban events.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchUnBlocks(self, request, context):
    """Subscribe to unblock events.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchUnWarns(self, request, context):
    """Subscribe to unwarn events.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchUnAdminJails(self, request, context):
    """Subscribe to admin jail release events.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchPlayerPunishments(self, request, context):
    """Subscribe to player punishments.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchPlayerAcquittals(self, request, context):
    """Subscribe to player acquittals.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchPunishments(self, request, context):
    """Subscribe to all punishments events.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchAcquittals(self, request, context):
    """Subscribe to all acquittals events.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MruVPunishmentsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Punish': grpc.unary_unary_rpc_method_handler(
          servicer.Punish,
          request_deserializer=punishments_dot_punishments__pb2.PunishRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.PunishResponse.SerializeToString,
      ),
      'Ban': grpc.unary_unary_rpc_method_handler(
          servicer.Ban,
          request_deserializer=punishments_dot_punishments__pb2.BanRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.BanResponse.SerializeToString,
      ),
      'Block': grpc.unary_unary_rpc_method_handler(
          servicer.Block,
          request_deserializer=punishments_dot_punishments__pb2.BlockRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.BlockResponse.SerializeToString,
      ),
      'Warn': grpc.unary_unary_rpc_method_handler(
          servicer.Warn,
          request_deserializer=punishments_dot_punishments__pb2.WarnRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.WarnResponse.SerializeToString,
      ),
      'AdminJail': grpc.unary_unary_rpc_method_handler(
          servicer.AdminJail,
          request_deserializer=punishments_dot_punishments__pb2.AdminJailRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.AdminJailResponse.SerializeToString,
      ),
      'MuteGlobalChats': grpc.unary_unary_rpc_method_handler(
          servicer.MuteGlobalChats,
          request_deserializer=punishments_dot_punishments__pb2.MuteGlobalChatsRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.MuteGlobalChatsResponse.SerializeToString,
      ),
      'UnBan': grpc.unary_unary_rpc_method_handler(
          servicer.UnBan,
          request_deserializer=punishments_dot_punishments__pb2.UnBanRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.UnBanResponse.SerializeToString,
      ),
      'UnBlock': grpc.unary_unary_rpc_method_handler(
          servicer.UnBlock,
          request_deserializer=punishments_dot_punishments__pb2.UnBlockRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.UnBlockResponse.SerializeToString,
      ),
      'UnWarn': grpc.unary_unary_rpc_method_handler(
          servicer.UnWarn,
          request_deserializer=punishments_dot_punishments__pb2.UnWarnRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.UnWarnResponse.SerializeToString,
      ),
      'UnAdminJail': grpc.unary_unary_rpc_method_handler(
          servicer.UnAdminJail,
          request_deserializer=punishments_dot_punishments__pb2.UnAdminJailRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.UnAdminJailResponse.SerializeToString,
      ),
      'UnMuteGlobalChats': grpc.unary_unary_rpc_method_handler(
          servicer.UnMuteGlobalChats,
          request_deserializer=punishments_dot_punishments__pb2.UnMuteGlobalChatsRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.UnMuteGlobalChatsResponse.SerializeToString,
      ),
      'GetPlayerBans': grpc.unary_unary_rpc_method_handler(
          servicer.GetPlayerBans,
          request_deserializer=punishments_dot_punishments__pb2.GetPlayerBansRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.GetPlayerBansResponse.SerializeToString,
      ),
      'GetPlayerWarns': grpc.unary_unary_rpc_method_handler(
          servicer.GetPlayerWarns,
          request_deserializer=punishments_dot_punishments__pb2.GetPlayerWarnsRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.GetPlayerWarnsResponse.SerializeToString,
      ),
      'GetPlayerAdminJail': grpc.unary_unary_rpc_method_handler(
          servicer.GetPlayerAdminJail,
          request_deserializer=punishments_dot_punishments__pb2.GetPlayerAdminJailRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.GetPlayerAdminJailResponse.SerializeToString,
      ),
      'GetBan': grpc.unary_unary_rpc_method_handler(
          servicer.GetBan,
          request_deserializer=punishments_dot_punishments__pb2.GetBanRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.BanMessage.SerializeToString,
      ),
      'GetWarn': grpc.unary_unary_rpc_method_handler(
          servicer.GetWarn,
          request_deserializer=punishments_dot_punishments__pb2.GetWarnRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.WarnMessage.SerializeToString,
      ),
      'GetBlock': grpc.unary_unary_rpc_method_handler(
          servicer.GetBlock,
          request_deserializer=punishments_dot_punishments__pb2.GetBlockRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.BlockMessage.SerializeToString,
      ),
      'IsPlayerBanned': grpc.unary_unary_rpc_method_handler(
          servicer.IsPlayerBanned,
          request_deserializer=punishments_dot_punishments__pb2.IsPlayerBannedRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.IsPlayerBannedResponse.SerializeToString,
      ),
      'IsCharacterBlocked': grpc.unary_unary_rpc_method_handler(
          servicer.IsCharacterBlocked,
          request_deserializer=punishments_dot_punishments__pb2.IsCharacterBlockedRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.IsCharacterBlockedResponse.SerializeToString,
      ),
      'IsCharacterJailed': grpc.unary_unary_rpc_method_handler(
          servicer.IsCharacterJailed,
          request_deserializer=punishments_dot_punishments__pb2.IsCharacterJailedRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.IsCharacterJailedResponse.SerializeToString,
      ),
      'WatchBans': grpc.unary_stream_rpc_method_handler(
          servicer.WatchBans,
          request_deserializer=punishments_dot_punishments__pb2.WatchBansRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.BanMessage.SerializeToString,
      ),
      'WatchBlocks': grpc.unary_stream_rpc_method_handler(
          servicer.WatchBlocks,
          request_deserializer=punishments_dot_punishments__pb2.WatchBlocksRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.BlockMessage.SerializeToString,
      ),
      'WatchWarns': grpc.unary_stream_rpc_method_handler(
          servicer.WatchWarns,
          request_deserializer=punishments_dot_punishments__pb2.WatchWarnsRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.WarnMessage.SerializeToString,
      ),
      'WatchAdminJails': grpc.unary_stream_rpc_method_handler(
          servicer.WatchAdminJails,
          request_deserializer=punishments_dot_punishments__pb2.WatchAdminJailsRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.AdminJailMessage.SerializeToString,
      ),
      'WatchUnBans': grpc.unary_stream_rpc_method_handler(
          servicer.WatchUnBans,
          request_deserializer=punishments_dot_punishments__pb2.WatchUnBansRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.UnBanMessage.SerializeToString,
      ),
      'WatchUnBlocks': grpc.unary_stream_rpc_method_handler(
          servicer.WatchUnBlocks,
          request_deserializer=punishments_dot_punishments__pb2.WatchUnBlocksRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.UnBlockMessage.SerializeToString,
      ),
      'WatchUnWarns': grpc.unary_stream_rpc_method_handler(
          servicer.WatchUnWarns,
          request_deserializer=punishments_dot_punishments__pb2.WatchUnWarnsRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.UnWarnMessage.SerializeToString,
      ),
      'WatchUnAdminJails': grpc.unary_stream_rpc_method_handler(
          servicer.WatchUnAdminJails,
          request_deserializer=punishments_dot_punishments__pb2.WatchUnAdminJailsRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.UnAdminJailMessage.SerializeToString,
      ),
      'WatchPlayerPunishments': grpc.unary_stream_rpc_method_handler(
          servicer.WatchPlayerPunishments,
          request_deserializer=punishments_dot_punishments__pb2.WatchPlayerPunishmentsRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.WatchPlayerPunishmentsResponse.SerializeToString,
      ),
      'WatchPlayerAcquittals': grpc.unary_stream_rpc_method_handler(
          servicer.WatchPlayerAcquittals,
          request_deserializer=punishments_dot_punishments__pb2.WatchPlayerAcquittalsRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.WatchPlayerAcquittalsResponse.SerializeToString,
      ),
      'WatchPunishments': grpc.unary_stream_rpc_method_handler(
          servicer.WatchPunishments,
          request_deserializer=punishments_dot_punishments__pb2.WatchPunishmentsRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.WatchPunishmentsResponse.SerializeToString,
      ),
      'WatchAcquittals': grpc.unary_unary_rpc_method_handler(
          servicer.WatchAcquittals,
          request_deserializer=punishments_dot_punishments__pb2.WatchAcquittalsRequest.FromString,
          response_serializer=punishments_dot_punishments__pb2.WatchAcquittalsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'mruv.punishments.MruVPunishmentsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
