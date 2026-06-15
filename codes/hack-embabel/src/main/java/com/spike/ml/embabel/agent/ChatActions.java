package com.spike.ml.embabel.agent;

import com.embabel.agent.api.annotation.Action;
import com.embabel.agent.api.annotation.EmbabelComponent;
import com.embabel.agent.api.common.ActionContext;
import com.embabel.chat.Conversation;
import com.embabel.chat.UserMessage;

//@EmbabelComponent
public class ChatActions {

//    @Action(canRerun = true, trigger = UserMessage.class)
    public void handleChat(Conversation conversation, ActionContext actionContext) {
        var assistantMessage = actionContext.ai()
                .withDefaultLlm()
                .withSystemPrompt("You are a helpful assistant. Answer questions concisely.")
                .respond(conversation.getMessages());
        actionContext.sendMessage(conversation.addMessage(assistantMessage));
    }
}
